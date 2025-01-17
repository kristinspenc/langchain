"""Test FastEmbed embeddings."""
import pytest

from langchain.embeddings.fastembed import FastEmbedEmbeddings


@pytest.mark.parametrize(
    "model_name", ["sentence-transformers/all-MiniLM-L6-v2", "BAAI/bge-small-en-v1.5"]
)
@pytest.mark.parametrize("max_length", [50, 512])
@pytest.mark.parametrize("doc_embed_type", ["default", "passage"])
@pytest.mark.parametrize("threads", [0, 10])
def test_fastembed_embedding_documents(
    model_name: str, max_length: int, doc_embed_type: str, threads: int
) -> None:
    """Test fastembed embeddings for documents."""
    documents = ["foo bar", "bar foo"]
    embedding = FastEmbedEmbeddings(
        model_name=model_name,
        max_length=max_length,
        doc_embed_type=doc_embed_type,
        threads=threads,
    )
    output = embedding.embed_documents(documents)
    assert len(output) == 2
    assert len(output[0]) == 384


@pytest.mark.parametrize(
    "model_name", ["sentence-transformers/all-MiniLM-L6-v2", "BAAI/bge-small-en-v1.5"]
)
@pytest.mark.parametrize("max_length", [50, 512])
def test_fastembed_embedding_query(model_name: str, max_length: int) -> None:
    """Test fastembed embeddings for query."""
    document = "foo bar"
    embedding = FastEmbedEmbeddings(model_name=model_name, max_length=max_length)
    output = embedding.embed_query(document)
    assert len(output) == 384


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "model_name", ["sentence-transformers/all-MiniLM-L6-v2", "BAAI/bge-small-en-v1.5"]
)
@pytest.mark.parametrize("max_length", [50, 512])
@pytest.mark.parametrize("doc_embed_type", ["default", "passage"])
@pytest.mark.parametrize("threads", [0, 10])
async def test_fastembed_async_embedding_documents(
    model_name: str, max_length: int, doc_embed_type: str, threads: int
) -> None:
    """Test fastembed embeddings for documents."""
    documents = ["foo bar", "bar foo"]
    embedding = FastEmbedEmbeddings(
        model_name=model_name,
        max_length=max_length,
        doc_embed_type=doc_embed_type,
        threads=threads,
    )
    output = await embedding.aembed_documents(documents)
    assert len(output) == 2
    assert len(output[0]) == 384


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "model_name", ["sentence-transformers/all-MiniLM-L6-v2", "BAAI/bge-small-en-v1.5"]
)
@pytest.mark.parametrize("max_length", [50, 512])
async def test_fastembed_async_embedding_query(
    model_name: str, max_length: int
) -> None:
    """Test fastembed embeddings for query."""
    document = "foo bar"
    embedding = FastEmbedEmbeddings(model_name=model_name, max_length=max_length)
    output = await embedding.aembed_query(document)
    assert len(output) == 384
