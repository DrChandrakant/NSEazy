#!/bin/bash
# Run this script test.sh from project root directory containing setup.py

set -ev

pr_branch=$1
if [ "${pr_branch}" == "false" ]
# All integrations pass if they're merged without a PR.
then
    exit 0
fi

echo "PR: branch passed in: $pr_branch"
# make sure we have the latest pip:
pip3 install --upgrade pip  

git fetch origin +refs/pull/${pr_branch}/merge
git checkout FETCH_HEAD
pip3 install .
pr_version=$(python3 -c "import nseazy; print(nseazy.__version__)")
git checkout main
pip3 install .
in_version=$(python3 -c "import nseazy; print(nseazy.__version__)")
echo "PR: ${pr_version}; Incumbent: ${in_version}"

# test the versions
git checkout FETCH_HEAD
pip3 install .
result=$(python3 scripts/check_version.py --pr_v ${pr_version} --in_v ${in_version})
if [ "${result}" != "VersionCheck:pr>main" ]
then
    # version in PR doesn't pass the test
    echo "${result}"
    exit 1
fi
echo "VersionCheck PASSED with response: ${result}"
