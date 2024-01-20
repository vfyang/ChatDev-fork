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
    - Key: b27ad5b6d481445495dafe897178f295
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
- [ ] 本地 LLM？
- [ ] Task 3 
- [ ] Task 4
