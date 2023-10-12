pyxgboost [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
~~[wheel](https://gitlab.com/KOLANICH/pyxgboost/-/jobs/artifacts/master/raw/wheels/pyxgboost-0.CI-py3-none-any.whl?job=build)~~
[![PyPi Status](https://img.shields.io/pypi/v/pyxgboost.svg)](https://pypi.python.org/pypi/pyxgboost)
~~![GitLab Build Status](https://gitlab.com/KOLANICH/pyxgboost/badges/master/pipeline.svg)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/pyxgboost/badges/master/coverage.svg)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/pyxgboost.svg)](https://libraries.io/github/KOLANICH/pyxgboost) [![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py) 

**We have moved to https://codeberg.org/KOLANICH-ML/pyxgboost, grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

This is a tool for conversion an [`xgboost`](https://github.com/dmlc/xgboost)[![PyPI version](https://badge.fury.io/py/xgboost.svg)](https://pypi.python.org/pypi/xgboost/)[![Build Status](https://github.com/dmlc/xgboost/workflows/XGBoost-CI/badge.svg?branch=master)](https://github.com/dmlc/xgboost/actions)[![docs](https://readthedocs.org/projects/xgboost/badge/?version=latest)](https://xgboost.readthedocs.org)[![Conda version](https://img.shields.io/conda/vn/conda-forge/py-xgboost.svg)](https://anaconda.org/conda-forge/py-xgboost)[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/dmlc/xgboost/badge)](https://api.securityscorecards.dev/projects/github.com/dmlc/xgboost)![License](https://img.shields.io/github/license/dmlc/xgboost.svg) tree into python AST or source.

The parsers residing in [`kaitai` dir](./pyxgboost/kaitai) are generated from [Kaitai Struct](https://github.com/kaitai-io/kaitai_struct) [definitions](https://codeberg.org/KOLANICH-specs/kaitai_struct_formats/tree/xgboost/scientific/data_science/dmlc) and since that have [Apache license](./pyxgboost/kaitai).

Requirements
------------
* [`kaitaistruct`](https://github.com/kaitai-io/kaitai_struct_python_runtime)
  [![PyPi Status](https://img.shields.io/pypi/v/kaitaistruct.svg)](https://pypi.python.org/pypi/kaitaistruct)
  ![License](https://img.shields.io/github/license/kaitai-io/kaitai_struct_python_runtime.svg) as a runtime for Kaitai Struct-generated code
  
* for old Pythons: some of the AST-to-source conversion libraries: [`astor`](https://github.com/berkerpeksag/astor)[![PyPi Status](https://img.shields.io/pypi/v/astor.svg)](https://pypi.python.org/pypi/astor)![License](https://img.shields.io/github/license/berkerpeksag/astor.svg), [`codegen`](https://github.com/andreif/codegen)[![PyPi Status](https://img.shields.io/pypi/v/codegen.svg)](https://pypi.python.org/pypi/codegen)![License](https://img.shields.io/github/license/andreif/codegen.svg), [`astunparse`](https://github.com/simonpercivall/astunparse)[![PyPi Status](https://img.shields.io/pypi/v/astunparse.svg)](https://pypi.python.org/pypi/astunparse)![License](https://img.shields.io/github/license/simonpercivall/astunparse.svg) and [`astmonkey`](https://github.com/mutpy/astmonkey)[![PyPi Status](https://img.shields.io/pypi/v/astmonkey.svg)](https://pypi.python.org/pypi/astmonkey)![License](https://img.shields.io/github/license/mutpy/astmonkey.svg).

* [`plumbum`](https://github.com/tomerfiliba/plumbum)
  [![PyPi Status](https://img.shields.io/pypi/v/plumbum.svg)](https://pypi.python.org/pypi/plumbum)
  [![Build Status](https://github.com/tomerfiliba/plumbum/workflows/CI/badge.svg)](https://github.com/tomerfiliba/plumbum/actions)
 [![Conda-forge](https://img.shields.io/conda/vn/conda-forge/plumbum.svg)](https://github.com/conda-forge/plumbum-feedstock)
 ![License](https://img.shields.io/github/license/tomerfiliba/plumbum.svg) - for command line interface
