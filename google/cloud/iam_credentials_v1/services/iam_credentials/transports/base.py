# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import abc
import typing
import pkg_resources

from google import auth
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore

from google.cloud.iam_credentials_v1.types import common


try:
    _client_info = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-iam",).version,
    )
except pkg_resources.DistributionNotFound:
    _client_info = gapic_v1.client_info.ClientInfo()


class IAMCredentialsTransport(abc.ABC):
    """Abstract transport class for IAMCredentials."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self,
        *,
        host: str = "iamcredentials.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
        quota_project_id: typing.Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                credentials_file, scopes=scopes, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = auth.default(
                scopes=scopes, quota_project_id=quota_project_id
            )

        # Save the credentials.
        self._credentials = credentials

        # Lifted into its own function so it can be stubbed out during tests.
        self._prep_wrapped_messages()

    def _prep_wrapped_messages(self):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.generate_access_token: gapic_v1.method.wrap_method(
                self.generate_access_token,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                ),
                default_timeout=60.0,
                client_info=_client_info,
            ),
            self.generate_id_token: gapic_v1.method.wrap_method(
                self.generate_id_token,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                ),
                default_timeout=60.0,
                client_info=_client_info,
            ),
            self.sign_blob: gapic_v1.method.wrap_method(
                self.sign_blob,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                ),
                default_timeout=60.0,
                client_info=_client_info,
            ),
            self.sign_jwt: gapic_v1.method.wrap_method(
                self.sign_jwt,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                    ),
                ),
                default_timeout=60.0,
                client_info=_client_info,
            ),
        }

    @property
    def generate_access_token(
        self,
    ) -> typing.Callable[
        [common.GenerateAccessTokenRequest],
        typing.Union[
            common.GenerateAccessTokenResponse,
            typing.Awaitable[common.GenerateAccessTokenResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def generate_id_token(
        self,
    ) -> typing.Callable[
        [common.GenerateIdTokenRequest],
        typing.Union[
            common.GenerateIdTokenResponse,
            typing.Awaitable[common.GenerateIdTokenResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def sign_blob(
        self,
    ) -> typing.Callable[
        [common.SignBlobRequest],
        typing.Union[
            common.SignBlobResponse, typing.Awaitable[common.SignBlobResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def sign_jwt(
        self,
    ) -> typing.Callable[
        [common.SignJwtRequest],
        typing.Union[common.SignJwtResponse, typing.Awaitable[common.SignJwtResponse]],
    ]:
        raise NotImplementedError()


__all__ = ("IAMCredentialsTransport",)
