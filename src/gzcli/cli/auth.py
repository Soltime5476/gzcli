import click
import yaml
from pathlib import Path
from gzcli.api._http import APIProfile
from gzcli.cli.config import PROFILES_PATH


def _load_profiles(fp: Path) -> dict:
    obj = yaml.safe_load(fp.read_text() if fp.is_file() else "")
    return obj if obj is not None else {}


def _save_edited_profiles(profiles: dict, fp: Path) -> None:
    fp.write_text(yaml.safe_dump(profiles) if profiles else "")


def _get_valid_profile(ctx, option, profile_name) -> APIProfile:
    all_profiles = _load_profiles(PROFILES_PATH)
    if profile_name not in all_profiles:
        raise click.BadParameter(f"profile {profile_name} does not exist")
    profile_obj = all_profiles[profile_name]
    profile_obj["name"] = profile_name
    return APIProfile.from_dict(profile_obj)


require_existing_profile = click.option(
    "--profile",
    default="default",
    required=True,
    callback=_get_valid_profile,
    help='the profile to use to connect to ctf server, "default" if unspecified',
)
