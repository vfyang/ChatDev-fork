# 学习小组的说明
以下是我们的中文注释，不要合并到源项目（原父 chatdev项目）
## 目标：
- 学习Multi-Agent框架，包括ChatDev，AutoGen
- 比较确认，如果需要更改，用开源的ChatDev，还是微软的AutoGen
- 确认如何用本地的语言模型？如中文
- 如何改为非变成任务？

### 环境：
- IDE：VS Code
- Python 环境： Conda
- Bug ： 试着用Github的Issues
- Group：微信群

### 资料：
- ChatDev 介绍： https://www.youtube.com/watch?v=SgKDPqDE964
- Microsoft Autogen ： https://www.youtube.com/watch?v=vU2S6dVf79M
- MS AutoGen Studio https://youtu.be/vU2S6dVf79M?si=N23IPDgcWf8Er8im
- crewAI：替代微软autogen、清华chatdev的新型多角色agent框架 
https://www.youtube.com/watch?v=TS8uS6Uhtek

### OpenAI 的key： 因为我们没有直接OpenAI Key，我们需要用Azure API key
- 需要测试如何设定，并正确调用 Azure API
- Azure OpenAI Key：
    - Endpoint:  https://gpt4-duan.openai.azure.com/
    - location : swedencentral
    - Key: ****************
    - Models： deployed models

| Model Name       | Model ID         | Code | Type     | Capacity |
|------------------|------------------|------|----------|----------|
| gpt-35-turbo     | gpt-35-turbo     | 0613 | Standard | 60K TPM  |
| Dalle3           | dall-e-3         | 3.0  | Standard | 1 CU     |
| gpt-35-turbo-16k | gpt-35-turbo-16k | 0613 | Standard | 60K TPM  |
| gpt-4            | gpt-4            | 0613 | Standard | 10K TPM  |

### 计划任务：
- [ ] 更改代码，该用 Azure OpenAI Key
- [ ] 测试 Pong Game 和 Flappy Bird
    -- python3 run.py --task "design a web version pong game" --name "Pong"
- [ ] 本地 LLM？
- [ ] Task 3 
- [ ] Task 4

### To Do：
线索： https://github.com/OpenBMB/ChatDev/pull/192

- Set OpenAI API Key: Export your OpenAI API key as an environment variable. Replace "your_OpenAI_API_key" with your actual API key. Remember that this environment variable is session-specific, so you need to set it again if you open a new terminal session. On Unix/Linux:
export OPENAI_API_TYPE="azure"
export OPENAI_API_VERSION="2023-12-01-preview"
export AZURE_OPENAI_ENDPOINT="https://gpt4-duan.openai.azure.com/"
export AZURE_OPENAI_KEY="****************"
export OPENAI_API_KEY="****************"

On Windows:

$env:OPENAI_API_KEY="****************"
export BASE_URL="https://gpt4-duan.openai.azure.com/"

```python
## Azure OpenAI API sample code:
#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 0.28.1 or lower.
import os
import openai

openai.api_type = "azure"
openai.api_base = "https://gpt4-duan.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

message_text = [{"role":"system","content":"You are a marketing writing assistant. You help come up with creative content ideas and content like marketing emails, blog posts, tweets, ad copy and product descriptions. You write in a friendly yet professional tone but can tailor your writing style that best works for a user-specified audience. If you do not know the answer to a question, respond by saying \"I do not know the answer to your question.\""}]

completion = openai.ChatCompletion.create(
  engine="gpt-4",
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)
```