"""Data models for the Account API category.

Mirrors src/GZCTF/Models/Request/Account in the GZ::CTF source.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional

from .enum import Role


class ModelWithCaptcha(BaseModel):
    """Abstract base carrying an optional captcha challenge token."""

    challenge: Optional[str] = None


class AccountVerifyModel(BaseModel):
    email: str = Field(min_length=1)
    token: str = Field(min_length=1)


class HashPowChallenge(BaseModel):
    challenge: str
    difficulty: int
    id: str


class LoginModel(ModelWithCaptcha):
    password: str = Field(min_length=1)
    userName: str = Field(min_length=1)


class MailChangeModel(BaseModel):
    newMail: str = Field(min_length=1)


class PasswordChangeModel(BaseModel):
    new: str = Field(min_length=6)
    old: str = Field(min_length=6)


class PasswordResetModel(BaseModel):
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)
    rToken: str = Field(min_length=1)


class ProfileUpdateModel(BaseModel):
    bio: Optional[str] = Field(default=None, max_length=128)
    phone: Optional[str] = None
    realName: Optional[str] = Field(default=None, max_length=128)
    stdNumber: Optional[str] = Field(default=None, max_length=64)
    userName: Optional[str] = Field(default=None, min_length=3, max_length=15)


class ProfileUserInfoModel(BaseModel):
    avatar: Optional[str] = None
    bio: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    realName: Optional[str] = None
    role: Optional[Role] = None
    stdNumber: Optional[str] = None
    userId: str
    userName: Optional[str] = None


class RecoveryModel(ModelWithCaptcha):
    email: str = Field(min_length=1)


class RegisterModel(ModelWithCaptcha):
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)
    userName: str = Field(min_length=3, max_length=15)
