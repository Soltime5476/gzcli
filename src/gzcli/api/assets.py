import contextlib
from pathlib import Path
from typing import Iterable
from gzcli.api._http import APIProfile, make_post


def upload_files(
    profile: APIProfile,
    file_paths: Iterable[Path],
):
    with contextlib.ExitStack() as stack:
        make_post(
            profile,
            "/api/assets",
            files=[
                ("files", stack.enter_context(f.open(mode="rb"))) for f in file_paths
            ],
        )
