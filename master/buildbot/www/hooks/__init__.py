from buildbot.www.hooks.base import ChangeHook, BaseChangeHook
from buildbot.www.hooks.bitbucket import BitBucketChangeHook
from buildbot.www.hooks.github import GitHubChangeHook
from buildbot.www.hooks.gitlab import GitLabChangeHook
from buildbot.www.hooks.gitorious import GitoriousChangeHook
from buildbot.www.hooks.googlecode import GoogleCodeChangeHook
from buildbot.www.hooks.poller import PollerChangeHook

hush_pyflakes = [ChangeHook, BaseChangeHook, BitBucketChangeHook,
                 GitHubChangeHook, GitLabChangeHook, GitoriousChangeHook,
                 GoogleCodeChangeHook, PollerChangeHook]
