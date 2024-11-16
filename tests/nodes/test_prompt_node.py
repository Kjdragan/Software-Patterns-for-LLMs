import pytest
from unittest.mock import patch, AsyncMock
from app.nodes_and_edges.nodes.prompt_node import prompt_node


@patch("app.nodes_and_edges.nodes.prompt_node.create_chat_prompt_template")
@pytest.mark.asyncio
async def test_prompt_node(mock_create_chat_prompt_template, state):
    """
    Test the async prompt_node function with mocked dependencies.
    """
    mock_prompt_template = AsyncMock()
    mock_prompt_template.ainvoke.return_value = "Mocked Prompt"
    mock_create_chat_prompt_template.return_value = mock_prompt_template

    updated_state = await prompt_node(state)

    assert updated_state["prompt"] == "Mocked Prompt"
    mock_create_chat_prompt_template.assert_called_once_with(
        state["context"], state["question"]
    )
    mock_prompt_template.ainvoke.assert_called_once_with(
        {
            "question": state["question"],
            "context": ["test1", "test2"],
        }
    )
