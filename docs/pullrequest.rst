.. _pullrequest:

Submit a pull request
=====================

To ask for a change you've made in your own Raspberry IO repository to
be merged into the official repository, you make a pull request. If
you're already familiar with Github and pull requests, just open a
pull request against the ``develop`` branch of the Raspberry IO
repository. (https://github.com/python/raspberryio/tree/develop) Be
sure that your code passes all tests, conforms to our :ref:`code standards
<codestandards>`, and has appropriate :ref:`documentation <documentation>`.

Read the rest of this document for more details.

Branch
------

Work on a branch from the `develop` branch.  Raspberry IO uses the
`Git Flow`_ system to manage branches and releases.  If you're using
the `gitflow tool`_, you can start your branch with:

.. code-block:: console

    $ git flow feature start NAME
    Switched to a new branch 'feature/NAME'

    Summary of actions:
    - A new branch 'feature/NAME' was created, based on 'develop'
    - You are now on branch 'feature/NAME'

    Now, start committing on your feature. When done, use:

         git flow feature finish NAME

    $

If you're not using the gitflow tool, create a new branch from
develop and switch to it:

.. code-block:: console

    $ git branch feature/NAME develop
    $ git checkout feature/NAME
    Switched to branch 'feature/NAME'
    $

Fork the repository
-------------------

Login to your Github account, then go to the `Raspberry IO repository`_
on Github and create a fork by clicking the ``Fork`` button near the
top right of the page.

Add a remote
------------

We'll assume you already have a local clone of the repository that
you've been working in, so all you need to do is add a new remote
definition pointing to your new fork. You might choose to name
your new remote definition using your Github username, to keep it
distinguished from the remote pointing at the official repository.

.. code-block:: console

    $ git remote add username git@github.com:username/raspberryio.git
    $ git remote -v
    username	git@github.com:username/raspberryio.git (fetch)
    username	git@github.com:username/raspberryio.git (push)
    origin	git://github.com/raspberryio/raspberryio.git (fetch)
    origin	git://github.com/raspberryio/raspberryio.git (push)
    $

Push your change to your own Github repository
----------------------------------------------

Your change needs to be on Github before you can open a pull request
against the Raspberry IO code. Unless you have Raspberry IO commit privileges,
you'll need to upload your change to your own fork of the repository.

Assuming your branch name is feature/NAME:

.. code-block:: console

    $ git push -u username feature/NAME
    Total 0 (delta 0), reused 0 (delta 0)
    To git@github.com:username/raspberryio.git
     * [new branch]      feature/NAME -> feature/NAME
    Branch feature/NAME set up to track remote branch feature/NAME from username.
    $

Open a pull request
-------------------

Go to your fork of the Raspberryio repository on the Github web site
(https://github.com/username/raspberryio/).

Click the ``Pull request`` button near the top center of the page.

Check the settings:

base repo
    python/raspberryio
base branch
    develop
head repo
    username/raspberryio (your repo)
head branch
    feature/NAME (your branch)

Enter an informative name and description for your pull request. By
default, Github will try to pull these from your commit messages, but
often you can improve them.

Your pull request description is your chance to convince people that
your change is worthwhile and will benefit Raspberry IO. Here are some
things to consider addressing:

* why is this change needed
* why will this be useful to general Raspberry IO users (not just you)
* what change was made
* why that change was made, as opposed to some other way of achieving the
  same ends
* what testing has been done
* etc.

Switch to the ``Files Changed`` tab and check that the changes shown are
what you expect. If not, go back and check that you've committed the
changes you intended on your branch, that you pushed it to your repo,
and that the pull request settings are correct for your repo and
branch.

When everything looks right, switch back to the ``New Pull Request``
tab and click the green ``Send pull request`` button in the lower
right, below the description box.

.. _Git Flow: http://nvie.com/posts/a-successful-git-branching-model/
.. _gitflow tool: https://github.com/nvie/gitflow
.. _Github: https://github.com
.. _Raspberry IO repository: https://github.com/python/raspberryio
