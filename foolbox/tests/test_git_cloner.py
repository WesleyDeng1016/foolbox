from foolbox.zoo import git_cloner
from pathlib import Path
import os
import hashlib
import pytest
from foolbox.zoo.git_cloner import GitCloneError


def test_git_clone():
    # given
    git_uri = "git@github.com:bethgelab/analysis-by-synthesis-model.git"
    expected_path = _expected_path(git_uri)

    # when
    path = git_cloner.clone(git_uri)

    # then
    assert path == expected_path


def test_wrong_git_uri():
    git_uri = "git@github.com:bethgelab/non-existing-repo.git"
    with pytest.raises(GitCloneError):
        git_cloner.clone(git_uri)


def _expected_path(git_uri):
    home = str(Path.home())
    m = hashlib.sha256()
    m.update(git_uri.encode())
    hash = m.hexdigest()
    expected_path = os.path.join(home, '.foolbox_zoo', hash)
    return expected_path
