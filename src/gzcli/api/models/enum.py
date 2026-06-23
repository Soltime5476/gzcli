"""Enumerations for the GZ::CTF API.

All enum types are defined as Pydantic-compatible Literal types. This mirrors
the definitions in GZCTF.Utils.Enums (https://github.com/GZTimeWalker/GZCTF/blob/develop/src/GZCTF/Utils/Enums.cs).
"""

from typing import Literal
from enum import IntFlag

# --- User/Auth ---------------------------------------------------------------

Role = Literal["Banned", "User", "Monitor", "Admin"]

RegisterStatus = Literal[
    "LoggedIn",
    "AdminConfirmationRequired",
    "EmailConfirmationRequired",
]

# --- Task/System Status ------------------------------------------------------

TaskStatus = Literal[
    "Unhealthy",
    "Degraded",
    "Pending",
    "Success",
    "Failed",
    "Duplicate",
    "Denied",
    "NotFound",
    "Exit",
]

# --- File/Container ----------------------------------------------------------

FileType = Literal["None", "Local", "Remote"]

ContainerStatus = Literal["Pending", "Running", "Destroyed"]

# --- Game/Challenge Notifications & Events ----------------------------------

NoticeType = Literal[
    "Normal",
    "FirstBlood",
    "SecondBlood",
    "ThirdBlood",
    "NewHint",
    "NewChallenge",
]

EventType = Literal[
    "Normal",
    "ContainerStart",
    "ContainerDestroy",
    "FlagSubmit",
    "CheatDetected",
]

# --- Submission/Answer -------------------------------------------------------

SubmissionType = Literal[
    "Unaccepted",
    "FirstBlood",
    "SecondBlood",
    "ThirdBlood",
    "Normal",
]

AnswerResult = Literal[
    "FlagSubmitted",
    "Accepted",
    "WrongAnswer",
    "CheatDetected",
    "NotFound",
]

# --- Participation -----------------------------------------------------------

ParticipationStatus = Literal[
    "Pending",
    "Accepted",
    "Rejected",
    "Suspended",
    "Unsubmitted",
]

# --- Challenge ---------------------------------------------------------------

ChallengeType = Literal[
    "StaticAttachment",
    "StaticContainer",
    "DynamicAttachment",
    "DynamicContainer",
]

ChallengeCategory = Literal[
    "Misc",
    "Crypto",
    "Pwn",
    "Web",
    "Reverse",
    "Blockchain",
    "Forensics",
    "Hardware",
    "Mobile",
    "PPC",
    "AI",
    "Pentest",
    "OSINT",
]

Difficulty = Literal[
    "Baby",
    "Trivial",
    "Easy",
    "Normal",
    "Medium",
    "Hard",
    "Expert",
    "Insane",
]

ChallengeNetworkMode = Literal["Open", "Isolated", "Custom"]

# --- Game Permissions (bit-flag integer) ------------------------------------


class GamePermission(IntFlag):
    JoinGame = 1
    RankOverall = 2
    RequireReview = 4
    ViewChallenge = 256
    SubmitFlags = 512
    GetScore = 1024
    GetBlood = 2048
    AffectDynamicScore = 4096
    All = 2147483647


# --- TimeStamp ------------------------------------
TimeStamp = int

# --- Captcha/Compression/CRUD ------------------------------------------------

CaptchaProvider = Literal["None", "HashPow", "CloudflareTurnstile"]

CompressionFormat = Literal["None", "GZip", "Zstd"]

ContainerPortMappingType = Literal["Default", "PlatformProxy"]

# --- Error Codes (constants) ------------------------------------------------


class ErrorCodes:
    """System error codes."""

    GameNotStarted: int = 10001
    GameEnded: int = 10002
