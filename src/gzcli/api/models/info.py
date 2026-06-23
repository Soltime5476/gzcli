"""Data models for the Info API category.

Mirrors src/GZCTF/Models/Request/Info in the GZ::CTF source.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional

from .enum import CaptchaProvider, ContainerPortMappingType


class ClientCaptchaInfoModel(BaseModel):
    siteKey: str
    type: CaptchaProvider


class ClientConfig(BaseModel):
    apiPublicKey: Optional[str] = None
    customTheme: Optional[str] = None
    defaultLifetime: int
    extensionDuration: int
    footerInfo: Optional[str] = None
    logoUrl: Optional[str] = None
    portMapping: ContainerPortMappingType
    renewalWindow: int
    slogan: str
    title: str


class PostDetailModel(BaseModel):
    authorAvatar: Optional[str] = None
    authorName: Optional[str] = None
    content: str = Field(min_length=1)
    id: str = Field(min_length=1)
    isPinned: bool
    summary: str = Field(min_length=1)
    tags: Optional[list[str]] = None
    time: int
    title: str = Field(min_length=1)


class PostInfoModel(BaseModel):
    authorAvatar: Optional[str] = None
    authorName: Optional[str] = None
    id: str = Field(min_length=1)
    isPinned: bool
    summary: str = Field(min_length=1)
    tags: Optional[list[str]] = None
    time: int
    title: str = Field(min_length=1)


class SignatureVerifyModel(BaseModel):
    publicKey: str = Field(min_length=1)
    teamToken: str = Field(min_length=1)


class TeamInfoModel(BaseModel):
    avatar: Optional[str] = None
    bio: Optional[str] = None
    id: int
    locked: bool
    members: Optional[list[TeamUserInfoModel]] = None
    name: Optional[str] = None


class TeamTransferModel(BaseModel):
    newCaptainId: str = Field(min_length=1)


class TeamUpdateModel(BaseModel):
    bio: Optional[str] = Field(default=None, max_length=72)
    name: Optional[str] = Field(default=None, max_length=20)


class TeamUserInfoModel(BaseModel):
    avatar: Optional[str] = None
    bio: Optional[str] = None
    captain: bool
    id: Optional[str] = None
    userName: Optional[str] = None
