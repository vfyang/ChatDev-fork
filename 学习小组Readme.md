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


### To Do：
线索： https://github.com/OpenBMB/ChatDev/pull/192

- Set OpenAI API Key: Export your OpenAI API key as an environment variable. Replace "your_OpenAI_API_key" with your actual API key. Remember that this environment variable is session-specific, so you need to set it again if you open a new terminal session. On Unix/Linux:
export OPENAI_API_TYPE="azure"
export OPENAI_API_VERSION="2023-12-01-preview"
export AZURE_OPENAI_ENDPOINT="https://gpt4-duan.openai.azure.com/"
export AZURE_OPENAI_KEY="****************"
export OPENAI_API_KEY="****************"

On Windows:
setx AZURE_OPENAI_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE"

### 计划任务：
- [x] 更改代码，该用 Azure OpenAI Key
- [x] 测试 Pong Game 和 Flappy Bird
    - python3 run.py --task "design a web version pong game" --name "Pong"
- [ ] 本地 LLM？
- [x] 测试 Dash Plotly，django 
    - Dash: 可以生成，但是错误的生成图表，而不是游戏。
    - django：不能生成子目录结构，入口错误的设置为 main.py, 而不是 manage.py
- [ ] 增量 修改已经生成的代码。
- [x] Visualizer
    - python visualizer/app.py  

## 帮助测试一下：我的Python需要重装，混乱了，可能是失败的原因，请帮我测一下
```shell
python run.py --task "Develop a Django-based website for managing checklists with an integrated user and task management system. Each task should include: Title, Description, Priority Level,Assignment, Ending Date. Utilize Bootstrap and Vue.js.  blue color theme. make sure all the django folder structure are setup correctly, and the main entrance python file should be manage.py instead of main.py" --name "Task_django_sub" --model "GPT_4_32K"

python run.py --task "Develop a dash based python  website for managing checklists with an integrated user and task management system. Each task should include: Title, Description, Priority Level,Assignment, Ending Date. Utilize Bootstrap and Vue.js.  blue color theme. make sure all the folder structure are setup correctly" --name "Task_dash_sub" --model "GPT_4_32K"