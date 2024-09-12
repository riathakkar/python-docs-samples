# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# TODO: Delete this file after approving /embeddings/retrievals_test.py
import backoff

from google.api_core.exceptions import ResourceExhausted

import embedding
import embedding_preview


@backoff.on_exception(backoff.expo, ResourceExhausted, max_time=10)
def test_embed_text_preview() -> None:
    texts = [
        "banana bread?",
        "banana muffin?",
        "banana?",
    ]
    dimensionality = 256
    embeddings = embedding_preview.embed_text(
        texts=texts,
        task="CODE_RETRIEVAL_QUERY",
        dimensionality=dimensionality,
    )
    assert [len(e) for e in embeddings] == [dimensionality or 768] * len(texts)


@backoff.on_exception(backoff.expo, ResourceExhausted, max_time=10)
def test_embed_text() -> None:
    texts = [
        "banana bread?",
        "banana muffin?",
        "banana?",
    ]
    dimensionality = 256
    embeddings = embedding.embed_text(texts, "RETRIEVAL_QUERY", dimensionality)
    assert [len(e) for e in embeddings] == [dimensionality or 768] * len(texts)
