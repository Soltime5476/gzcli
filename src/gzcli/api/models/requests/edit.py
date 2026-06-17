from pydantic import BaseModel, Field
from typing import Literal, Optional

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

ChallengeType = Literal[
    "StaticAttachment",
    "StaticContainer",
    "DynamicAttachment",
    "DynamicContainer",
]

ChallengeNetworkMode = Literal["Open", "Isolated", "Custom"]

FileType = Literal["None", "Local", "Remote"]

ContainerStatus = Literal["Pending", "Running", "Destroyed"]


class Attachment(BaseModel):
    id: int
    type: FileType
    fileSize: Optional[int] = None
    url: Optional[str] = None


class AttachmentCreateModel(BaseModel):
    attachmentType: FileType
    fileHash: Optional[str] = None
    url: Optional[str] = None


class RequestResponse(BaseModel):
    status: int
    title: str


class FlagInfoModel(BaseModel):
    attachment: Optional[Attachment] = None
    flag: str
    id: int


class ChallengeUpdateModel(BaseModel):
    category: Optional[ChallengeCategory] = None
    containerImage: Optional[str] = None
    content: Optional[str] = None
    cpuCount: Optional[int] = Field(default=None, ge=1, le=1024)
    deadlineUtc: Optional[int] = None
    difficulty: Optional[float] = None
    disableBloodBonus: bool = False
    enableTrafficCapture: Optional[bool] = None
    exposePort: Optional[int] = None
    fileName: Optional[str] = None
    flagTemplate: Optional[str] = Field(default=None, max_length=120)
    hints: Optional[list[str]] = None
    isEnabled: Optional[bool] = None
    memoryLimit: Optional[int] = None
    minScoreRate: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    networkMode: Optional[ChallengeNetworkMode] = None
    originalScore: Optional[int] = None
    storageLimit: Optional[int] = None
    submissionLimit: Optional[int] = Field(default=None, ge=0, le=10000)
    testContainer: Optional[ContainerInfoModel] = None
    title: Optional[str] = Field(default=None, min_length=1)
    type: Optional[ChallengeType] = None


class ChallengeInfoModel(BaseModel):
    title: str = Field(min_length=1)
    category: ChallengeCategory
    deadlineUtc: Optional[int] = None
    id: Optional[int] = None
    isEnabled: Optional[bool] = None
    minScore: Optional[int] = None
    originalScore: Optional[int] = None
    score: Optional[int] = None
    type: ChallengeType


class ChallengeEditDetailModel(BaseModel):
    acceptedCount: int
    category: ChallengeCategory
    content: str
    cpuCount: Optional[int] = Field(default=None, ge=1, le=1024)
    containerImage: str
    difficulty: float
    flags: list[FlagInfoModel]
    isEnabled: bool
    minScoreRate: float = Field(ge=0.0, le=1.0)
    originalScore: int
    submissionLimit: int
    title: str = Field(min_length=1)
    type: ChallengeType
    attachment: Optional[Attachment] = None

    deadlineUtc: Optional[int] = None
    disableBloodBonus: Optional[bool] = None
    enableTrafficCapture: Optional[bool] = None
    exposePort: Optional[int] = None
    fileName: Optional[str] = None
    flagTemplate: Optional[str] = Field(default=None, max_length=120)
    hints: list[str]
    id: int
    memoryLimit: Optional[int] = None
    networkMode: ChallengeNetworkMode = "Open"
    storageLimit: Optional[int] = None
    testContainer: Optional[ContainerInfoModel] = None


class FlagCreateModel(BaseModel):
    flag: str = Field(min_length=1, max_length=127)
    attachmentType: Optional[FileType] = None
    fileHash: Optional[str] = None
    remoteUrl: Optional[str] = None


class ContainerInfoModel(BaseModel):
    entry: str
    expectStopAt: int
    startedAt: int
    status: ContainerStatus
