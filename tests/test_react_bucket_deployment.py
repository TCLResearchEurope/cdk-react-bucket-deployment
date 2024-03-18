from pathlib import Path

import pytest

from aws_cdk import App
from aws_cdk import Stack
from aws_cdk.aws_s3 import Bucket
from react_bucket_deployment import ReactBucketDeployment


@pytest.fixture
def cdk_app() -> App:
    return App()


@pytest.fixture
def cdk_stack(cdk_app: App) -> Stack:
    return Stack(cdk_app, "TestStack")


@pytest.fixture
def s3_bucket(cdk_stack: Stack) -> Bucket:
    return Bucket(cdk_stack, "TestBucket")


@pytest.fixture
def react_project_dir(tmp_path: Path) -> Path:
    path = tmp_path / "react-project"
    path.mkdir()
    return path


@pytest.fixture
def build_dir(react_project_dir: Path) -> Path:
    return react_project_dir / "build"


@pytest.fixture(autouse=True)
def prepare_source_code(react_project_dir: Path) -> None:
    template_path = Path(__file__).parent / "resources" / "package_template.json"
    template_lock_path = (
        Path(__file__).parent / "resources" / "package_lock_template.json"
    )

    (react_project_dir / "package.json").write_text(template_path.read_text())
    (react_project_dir / "package-lock.json").write_text(template_lock_path.read_text())


def test_build_project(
    cdk_stack: Stack, react_project_dir: Path, build_dir: Path, s3_bucket: Bucket
) -> None:
    ReactBucketDeployment(
        cdk_stack,
        "DeployReactApp",
        sources=str(react_project_dir),
        destination_bucket=s3_bucket,
    )

    assert build_dir.exists()
    assert (build_dir / "index.html").exists()


def test_build_artifacts_presence(
    cdk_stack: Stack, react_project_dir: Path, build_dir: Path, s3_bucket: Bucket
) -> None:
    ReactBucketDeployment(
        cdk_stack,
        "DeployReactApp",
        sources=str(react_project_dir),
        destination_bucket=s3_bucket,
    )
