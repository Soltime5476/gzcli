from pydantic import BaseModel, Field
from typing import Optional


class TeamUpdateModel(BaseModel):
    """Team information used to create or update a team."""

    name: Optional[str] = Field(default=None, max_length=20)
    bio: Optional[str] = Field(default=None, max_length=72)


class TeamUserInfoModel(BaseModel):
    """Information about a single team member."""

    captain: bool = False
    id: Optional[str] = None
    userName: Optional[str] = None
    bio: Optional[str] = None
    avatar: Optional[str] = None


class TeamInfoModel(BaseModel):
    """Team information returned by the server."""

    id: int
    locked: bool = False
    name: Optional[str] = None
    bio: Optional[str] = None
    avatar: Optional[str] = None
    members: Optional[list[TeamUserInfoModel]] = None
