# Django Drive

An exercise in Django.

## Project overview

Create a Django project for simulating a file sharing system.

This repository contains the basic elements for starting the project, including:

- A `requirements.txt` file to install dependencies with `pip`. (A virtual environment is recommended.)
- A blank Django project with default admin authentication setup enabled.
- A `.gitignore` that ignores common files that should not be committed.

The setup has been tested on Python 3.9 on Ubuntu Linux, but should work on newer versions as well.

## Solution submission

Please fork this repository privately on GitLab, and commit your solutions there.
Make sure that I have access to read.

Levels and bonus target should be tagged according to the instructions for each.

## Requirements

### Models

The project requires 3 abstraction that should be modelled:

- `Drive`
- `Directory`
- `File`

Each must have a `name` set.

Furthermore, we have the following requirements:

- A `Drive` has an `owner` which is a `User`.
- A `Directory` may be in the root of its `Drive` or a subdirectory of another `Directory`.
- A `File` may be in the root of its `Drive` or in a `Directory`.
- A `File` is always a text file.

Should you desire so, you may add, remove or change models as you desire, as long as the end goal is achieved.
It is for example perfectly valid to _not_ create the `Drive` as a class, and use a `Directory` model in some form instead.
You may also subclass and make model abstractions as you like.

You do not need to implement everything right at once. In fact it is better if at least the levels are in separate commit to be able to assess progress them better.

You do not need to store a file on disk for every added file.

Do not worry about migrations being consecutive. You may delete all migrations and regenerate for each commit if you'd like.

### Frontend

Here is an overview of the required paths for the frontend.

| Path               | Purpose           |
| ------------------ | ----------------- |
| `/`                | Drive listing     |
| `/drive/<id>/`     | Drive content     |
| `/directory/<id>/` | Directory content |
| `/file/<id>/`      | File content      |

You may apply any frontend framework you desire, or none at all.

You may provide login as you like through the admin or your own form.

## Levels

In these section are the levels that you may complete.

Please tag your levels completions in your forked repository in the form `level_N` where `N` is the level number.

### Level 1 - Models and Admin

- Setup basic models with relationships to model the requirements. Do not worry too much about constraints, relationship is key.
- Each model, must be added to the Django admin so data can be added, changed and deleted.

### Level 2 - Basic display

Disregard drive owners for now.

- Present all drives in the listing at `/` with links to their `/drive/<id>/` page.
- Present the content of each drive under it's `/drive/<id>/` page with links to file and directory pages.
- Present directories in the same manner, but with a link back to the drive or a parent directory.
- Present file content with a link back to the directory.

### Level 3 - Access to Frontend

- Each drive must have an owner.
- Make the frontend redirect to login when not logged in.
- Make the listing only show the user's accessible drives
- Superuser can see all drives.
- Superusers get the username shown by each drive.

## Stretch targets

Below are stretch targets listed with the level they require completed before.

Please tag your stretch target completions in your forked repository with the key starting each target.

No level requirement:

- `black`: Setup a pipeline fo each commit to check that the code conforms to the newest version of `black`.
- `isort`: Setup a pipeline fo each commit to check that the code conforms to the newest version of `isort`.

Level 1:

- `uuid`: Use UUID for primary keys.

Level 2:

- `edit_name`: Make it possible to rename viewed files, drives and directories.
- `edit_file`:Make files editable.

Level 3:

- Expose models in a REST API using [Django REST framework](https://www.django-rest-framework.org/). You must support Basic authentication.
- `CRUD`: Make it possible to add and delete items on drives that you own in the frontend.
- `reader_access`: Make it possible to assign reader access to your a `Drive` or `Directory` for other users.
- `public_access`: Make it possible to mark a `Drive` and/or `Directory` as _Private_, _Public_ or _Hidden public_.
  Rules:
  - _Public_ means that anyone can view the content and see it in the listing.
  - _Hidden public_ is like _Public_, except it is not listed

**Note:** If you complete one or both of the stretch goals `reader_access` and `public_access`, try to make it clear in the listing what is what, by listing in sections and providing meta data.
