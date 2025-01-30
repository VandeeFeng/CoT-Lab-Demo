# lang.py
LANGUAGE_CONFIG = {
    "en": {
        "title": "CoT-Lab: Human-AI Co-Thinking Laboratory \nFollow, learn, and iterate the thought within one turn.",
        "prompt_label": "Task Description - Prompt",
        "prompt_placeholder": "Enter your prompt here...",
        "editor_label": "Thought Editor",
        "editor_placeholder": "The AI's thinking process will appear here... You can edit when it pauses",
        "generate_btn": "Generate",
        "pause_btn": "Pause",
        "sync_threshold_label": "🧠 Human Thinking Cadence",
        "sync_threshold_info": "Pause for human turn per X paragraphs",
        "throughput_label": "⏱ Sync Rate",
        "throughput_info": "Tokens/s - 5:Learn, 10:Follow, 50:Skim",
        "language_label": "Language",
        "loading_thinking": "🤖 AI Thinking...<br>Shift+Enter to Pause",
        "loading_output": "🖨️ Result Writing...<br>Shift+Enter to Pause",
        "interrupted": "🤔 Pause, Human thinking time <br>Shift+Enter to hand over to AI",
        "completed": "✅ Completed <br> Find formatted final result in results tab",
        "error": "Error",
        "api_config_label": "API Configuration",
        "api_key_label": "API Key",
        "api_key_placeholder": "Leave empty to use environment variable",
        "api_url_label": "API URL",
        "api_url_placeholder": "Leave empty for default URL",
        "clear_btn": "Clear Thinking",
        "introduction": "Think together with AI. Use `Shift+Enter` to toggle generation <br>You can modify the thinking process when AI pauses",
        "bot_label": "Conversation Overview",
        "bot_default": [
            {
                "role": "assistant",
                "content": "Welcome to our co-thinking space! Ready to synchronize our cognitive rhythms? \n Shall we start by adjusting the throughput slider to match your reading pace? \n Enter your task below, edit my thinking process when I pause, and let's begin weaving thoughts together →",
            },
        ],
    },
    "zh": {
        "title": "CoT-Lab: 人机协同思维实验室\n在一轮对话中跟随、学习、迭代思维链",
        "prompt_label": "任务描述 - 提示词",
        "prompt_placeholder": "在此输入您的问题...",
        "editor_label": "思维编辑器",
        "editor_placeholder": "AI的思考过程将在此显示...您可以在暂停的时候编辑",
        "generate_btn": "生成",
        "pause_btn": "暂停",
        "sync_threshold_label": "🧠 人类思考间隔",
        "sync_threshold_info": "段落数 - 每X段落自动暂停进入人类思考时间",
        "throughput_label": "⏱ 同步思考速度",
        "throughput_info": "词元/秒 - 5:学习, 10:跟读, 50:跳读",
        "language_label": "界面语言",
        "loading_thinking": "🤖 AI思考中... <br>Shift+Enter可暂停",
        "loading_output": "🖨️ 结果输出中... <br>Shift+Enter可暂停",
        "interrupted": "🤔 暂停，人类思考回合<br>Shift+Enter交回给AI",
        "completed": "✅ 已完成 <br> 可在结果标签页中查看渲染了格式的最终结果",
        "error": "错误",
        "api_config_label": "API配置",
        "api_key_label": "API密钥",
        "api_key_placeholder": "留空使用环境变量",
        "api_url_label": "API地址",
        "api_url_placeholder": "留空使用默认地址",
        "clear_btn": "清空思考",
        "introduction": "和AI一起思考，Shift+Enter切换生成状态<br>AI暂停的时候你可以编辑思维过程",
        "bot_label": "对话一览",
        "bot_default": [
            {
                "role": "assistant",
                "content": "欢迎来到协同思考空间！准备好同步我们的认知节奏了吗？\n 建议先调整右侧的'同步思考速度'滑块，让它匹配你的阅读速度 \n 在下方输入任务描述，在我暂停时修改我的思维，让我们开始编织思维链条 →",
            },
            {"role": "assistant", "content": "**Shift+Enter** 可以暂停/继续AI生成"},
        ],
    },
}
