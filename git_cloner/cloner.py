# -*- coding: UTF-8 -*-

# 在Python3.0测试通过
# 需要在gitlab里面新建一个AccessToken填入gitlabToken

import os
import sys
import time
import json
import shlex
import argparse
import subprocess

if sys.version_info < (3, 0):
  from urllib2 import Request, urlopen
else:
  from urllib.request import Request, urlopen


def get_flags():
  os.environ['COLUMNS'] = "132"
  cmd = argparse.ArgumentParser()
  cmd.add_argument('-s', '--server', type=str, required=True, metavar='<url>',
                   help='The GitLab server url')
  cmd.add_argument('-u', '--user', type=str, required=True, metavar='<user>',
                   help='The GitLab login username')
  cmd.add_argument('-p', '--pass', type=str, required=True, metavar='<pass>',
                   help='The GitLab login password')
  cmd.add_argument('-g', '--group', type=str, nargs='+', metavar='<group>',
                   help='Only clone the projects in this group(s)')
  cmd.add_argument('-o', '--output', type=str, metavar='<path>',
                   help='Clone projects to output directory')
  return cmd.parse_args()


def access_token(server, username, password):
  url = "%s/oauth/token" % server
  data = "grant_type=password&username=%s&password=%s" % (username, password)
  request = Request(url, data=data.encode(), headers={"Accept": "application/json"})
  response = json.loads(urlopen(request).read().decode(encoding='UTF-8'))
  if not response or not response.get('access_token'):
    raise ValueError('Invalid username/password!')
  return str(response['access_token'])


def clone_projects(server, token, group, output):
  count = 0
  page_idx = 1
  page_size = 100
  while True:
    url = "%s/api/v4/groups/%s/projects?access_token=%s&per_page=%d&page=%d&order_by=name" % (
      server, group, token, page_size, page_idx
    )
    request = urlopen(url)
    response = json.loads(request.read().decode(encoding='UTF-8'))
    if not response or len(response) == 0:
      break
    page_idx += 1
    for project in response:
      git_url = project['http_url_to_repo']
      git_url = git_url.replace('http://10.248.249.33:8081/', 'https://gitlab.trip.epec.com/')
      git_dir = os.path.join(output, project['path_with_namespace'])
      if git_url.endswith(".old") or git_dir.endswith(".old"):
        continue
      try:
        print("Cloning project '%s' to '%s'..." % (git_url, git_dir))
        if os.path.exists(git_dir):
          command = shlex.split('git -c "%s" pull' % git_dir)
        else:
          command = shlex.split('git clone %s "%s"' % (git_url, git_dir))
        rt = subprocess.Popen(command).wait()
        if rt:
          print("Clone project '%s' to '%s' return %d" % (git_url, git_dir, rt))
        count += 1
      except Exception as ex:
        print("Clone project '%s' to '%s' error: %s" % (git_url, git_dir, ex))
  return count


def main():
  flags = get_flags()
  output = flags.output or os.getcwd()
  token = access_token(flags.server, flags.user, getattr(flags, 'pass'))
  print("GitLab clone start to clone project from %s for groups %s..." % (flags.server, flags.group))
  for group in flags.group or []:
    print("Cloning all projects for group '%s'..." % group)
    count = clone_projects(flags.server, token, group, output)
    print("Cloned %d projects for group '%s'." % (count, group))


if __name__ == '__main__':
  main()
