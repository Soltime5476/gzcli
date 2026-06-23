"""Data models for the Admin API category.

Mirrors src/GZCTF/Models/Request/Admin in the GZ::CTF source.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional

from .account import ProfileUserInfoModel
from .data import ApiToken
from .enum import ChallengeCategory, ParticipationStatus, Role, TaskStatus
from .game import TeamModel
from .info import TeamInfoModel


class AccountPolicy(BaseModel):
    activeOnRegister: bool
    allowRegister: bool
    emailConfirmationRequired: bool
    emailDomainList: str
    useCaptcha: bool


class AdminTeamModel(BaseModel):
    bio: Optional[str] = Field(default=None, max_length=72)
    locked: Optional[bool] = None
    name: Optional[str] = Field(default=None, max_length=20)


class AdminUserInfoModel(BaseModel):
    bio: Optional[str] = Field(default=None, max_length=128)
    email: Optional[str] = None
    emailConfirmed: Optional[bool] = None
    phone: Optional[str] = None
    realName: Optional[str] = Field(default=None, max_length=128)
    role: Optional[Role] = None
    stdNumber: Optional[str] = Field(default=None, max_length=64)
    userName: Optional[str] = Field(default=None, min_length=3, max_length=15)


class ApiTokenCreateModel(BaseModel):
    expiresIn: Optional[int] = None
    name: str = Field(min_length=1, max_length=128)


class ApiTokenResponse(BaseModel):
    info: ApiToken
    token: str


class ChallengeModel(BaseModel):
    category: ChallengeCategory
    id: int
    title: str


class ConfigEditModel(BaseModel):
    accountPolicy: Optional[AccountPolicy] = None
    containerPolicy: Optional[ContainerPolicy] = None
    globalConfig: Optional[GlobalConfig] = None


class ContainerInstanceModel(BaseModel):
    challenge: Optional[ChallengeModel] = None
    containerGuid: str
    containerId: str
    expectStopAt: int
    image: str
    ip: str
    port: int
    startedAt: int
    team: Optional[TeamModel] = None


class ContainerPolicy(BaseModel):
    autoDestroyOnLimitReached: bool
    defaultLifetime: int = Field(ge=1, le=7200)
    extensionDuration: int = Field(ge=1, le=7200)
    maxExerciseContainerCountPerUser: int
    renewalWindow: int = Field(ge=1, le=360)


class GlobalConfig(BaseModel):
    apiEncryption: bool
    customTheme: Optional[str] = None
    description: Optional[str] = None
    faviconHash: Optional[str] = None
    footerInfo: Optional[str] = None
    logoHash: Optional[str] = None
    slogan: str
    title: str


class LogMessageModel(BaseModel):
    ip: Optional[str] = None
    level: Optional[str] = None
    msg: Optional[str] = None
    name: Optional[str] = None
    status: Optional[TaskStatus] = None
    time: int


class ParticipationEditModel(BaseModel):
    divisionId: Optional[int] = None
    status: Optional[ParticipationStatus] = None


class ParticipationInfoModel(BaseModel):
    divisionId: Optional[int] = None
    id: int
    registeredMembers: list[str]
    status: ParticipationStatus
    team: TeamWithDetailedUserInfo


class TeamWithDetailedUserInfo(BaseModel):
    avatar: Optional[str] = None
    bio: Optional[str] = None
    captainId: str
    id: int
    locked: bool
    members: list[ProfileUserInfoModel]
    name: Optional[str] = None


class UserCreateModel(BaseModel):
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)
    phone: Optional[str] = None
    realName: Optional[str] = Field(default=None, max_length=128)
    stdNumber: Optional[str] = Field(default=None, max_length=64)
    teamName: Optional[str] = Field(default=None, max_length=20)
    userName: str = Field(min_length=3, max_length=15)


class UserInfoModel(BaseModel):
    avatar: Optional[str] = None
    bio: Optional[str] = None
    email: Optional[str] = None
    emailConfirmed: Optional[bool] = None
    id: Optional[str] = None
    ip: str
    lastVisitedUtc: int
    phone: Optional[str] = None
    realName: Optional[str] = None
    registerTimeUtc: int
    role: Optional[Role] = None
    stdNumber: Optional[str] = None
    userName: Optional[str] = None


class WriteupInfo(BaseModel):
    divisionId: Optional[int] = None
    id: int
    team: TeamInfoModel
    uploadTimeUtc: int
    url: str


class WriteupInfoModel(BaseModel):
    divisions: dict[str, str]
    writeups: list[WriteupInfo]
