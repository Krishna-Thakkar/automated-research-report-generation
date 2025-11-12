# 📊 Automated Report Generation

> An intelligent research assistant that automatically generates comprehensive, well-structured reports using AI-powered analyst agents, web research, and human feedback.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-orange.svg)](https://langchain-ai.github.io/langgraph/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 Overview

**Automated Report Generation** is a sophisticated research automation system that leverages LangGraph workflow orchestration to create detailed, professional reports on any given topic. The system creates intelligent analyst agents that conduct web research, generate interview-style Q&A sessions, and compile comprehensive reports with structured sections.

The platform features a complete web interface with user authentication, real-time progress tracking, and multi-format report output (PDF and DOCX), making it ideal for researchers, content creators, and analysts who need high-quality reports quickly.

---

## ✨ Features

- 🤖 **AI-Powered Analyst Agents**: Automatically creates specialized analyst personas based on your topic
- 🔍 **Intelligent Web Research**: Uses Tavily API to gather real-time information from the web
- 👥 **Human-in-the-Loop**: Integrates user feedback to refine research direction
- 📝 **Multi-Section Reports**: Generates structured reports with introduction, body sections, and conclusion
- 📄 **Multi-Format Output**: Exports reports in both PDF and DOCX formats
- 🔐 **Secure Authentication**: User signup/login with encrypted password storage
- 🎯 **Modular Workflow**: Built with reusable LangGraph nodes for easy customization
- 🗄️ **Data Persistence**: SQLite database for user management
- 📁 **Organized Storage**: Timestamped folders for each generated report

---

## 🏗️ Architecture

### System Workflow

The application follows a sophisticated multi-stage workflow orchestrated by LangGraph:

![Alt Text](assets/system_workflow.png)

### Component Architecture

![Alt Text](assets/component_architecture.png)

---

## 📂 Project Structure

```
automated-report-generation/
│
├── research_and_analyst/           # Main application package
│   ├── api/                        # FastAPI application
│   │   ├── main.py                 # FastAPI app entry point
│   │   ├── models/                 # Request/response models
│   │   │   └── request_models.py
│   │   ├── routes/                 # API endpoints
│   │   │   └── report_routes.py
│   │   ├── services/               # Business logic
│   │   │   └── report_service.py
│   │   └── templates/              # HTML templates
│   │       ├── dashboard.html      # Main dashboard
│   │       ├── login.html          # Login page
│   │       ├── signup.html         # User registration
│   │       └── report_progress.html # Progress tracking
│   │
│   ├── workflows/                  # LangGraph workflow definitions
│   │   ├── interview_workflow.py   # Interview Q&A generation
│   │   └── report_generator_workflow.py  # Main report workflow
│   │
│   ├── config/                     # Configuration files
│   │   └── configuration.yaml      # App settings
│   │
│   ├── database/                   # Database management
│   │   └── db_config.py            # SQLite setup
│   │
│   ├── schemas/                    # Data models
│   │   └── models.py               # Pydantic schemas
│   │
│   ├── utils/                      # Utility functions
│   │   ├── config_loader.py        # Config management
│   │   └── model_loader.py         # LLM initialization
│   │
│   ├── prompt_lib/                 # Prompt templates
│   │   └── prompt_locator.py
│   │
│   ├── logger/                     # Logging configuration
│   │   └── custom_logger.py
│   │
│   ├── exception/                  # Custom exceptions
│   │   └── custom_exception.py
│   │
│   └── notebook/                   # Development notebooks
│       └── test.ipynb
│
├── static/                         # Frontend assets
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js
│
├── templates/                      # Additional templates
│
├── generated_report/               # Output directory
│   └── [Topic_Timestamp]/          # Individual report folders
│       ├── [Report].pdf
│       └── [Report].docx
│
├── logs/                           # Application logs
│
├── users.db                        # SQLite database
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project metadata
├── main.py                         # CLI entry point
└── README.md                       # Project documentation
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Krishna-Thakkar/automated-research-report-generation.git
   cd automated-research-report-generation
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   
   Create a `.env` file in the root directory:
   ```env
   # LLM API Keys
   GROQ_API_KEY=your_groq_api_key
   GOOGLE_API_KEY=your_google_api_key

   # Web Search API
   TAVILY_API_KEY=your_tavily_api_key
   ```

---

## 🎯 How It Works

### Workflow Breakdown

#### 1. **User Authentication**
- Users sign up with encrypted credentials stored in SQLite
- Login authentication validates user access
- Session management ensures secure access

#### 2. **Topic Submission**
- User enters research topic on dashboard
- Provides optional feedback/direction for research focus
- System validates and queues the request

#### 3. **Analyst Creation**
- LangGraph creates a specialized analyst agent
- Agent is configured based on topic and user feedback
- Persona includes expertise area and research focus

#### 4. **Interview Workflow**
The system executes a cyclical interview process:

```python
# Interview Graph Nodes
builder.add_node("ask_question", self._generate_question)
builder.add_node("search_web", self._search_web)
builder.add_node("generate_answer", self._generate_answer)
builder.add_node("save_interview", self._save_interview)
builder.add_node("write_section", self._write_section)
```

- **Generate Question**: Creates relevant research questions
- **Search Web**: Uses Tavily to gather real-time information
- **Generate Answer**: Synthesizes findings into coherent answers
- **Save Interview**: Stores Q&A pairs for reference
- **Write Section**: Compiles information into report sections

#### 5. **Report Compilation**
Main workflow orchestrates final report assembly:

```python
# Report Generation Nodes
builder.add_node("create_analyst", self.create_analyst)
builder.add_node("human_feedback", self.human_feedback)
builder.add_node("conduct_interview", interview_graph)
builder.add_node("write_report", self.write_report)
builder.add_node("write_introduction", self.write_introduction)
builder.add_node("write_conclusion", self.write_conclusion)
builder.add_node("finalize_report", self.finalize_report)
```

#### 6. **Multi-Format Export**
- Report is converted to PDF using ReportLab
- DOCX version created using python-docx
- Both files saved in timestamped folder

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Workflow Orchestration** | LangGraph | Multi-agent workflow management |
| **Web Framework** | FastAPI | REST API and web interface |
| **Database** | SQLite | User data and session storage |
| **LLM Integration** | Google/Groq | AI-powered content generation |
| **Web Search** | Tavily API | Real-time web research |
| **Document Generation** | python-docx, ReportLab | DOCX and PDF creation |
| **Frontend** | HTML/CSS | User interface |
| **Authentication** | bcrypt | Password encryption |
| **Configuration** | YAML, python-dotenv | Settings management |

---

## 💻 Usage

### Starting the Application

1. **Launch the FastAPI Server**
   ```bash
   uvicorn research_and_analyst.api.main:app --host 0.0.0.0 --port 8000
   ```

2. **Access the Application**
   - Open browser: `http://localhost:8000`
   - Navigate to signup page to create account
   - Login with credentials

### Generating a Report

1. **Login to Dashboard**
   - Enter your credentials
   - Access main dashboard

2. **Submit Research Topic**
   ```
   Topic: "Impact of Generative AI on Jobs"
   Feedback: "Focus on 2024-2025 trends and industry-specific impacts"
   ```

3. **Monitor Progress**
   - Real-time status updates displayed
   - View current workflow stage
   - Estimated completion time

4. **Download Report**
   - Report automatically saved in `generated_report/` directory
   - Access both PDF and DOCX versions
   - Folder named: `[Topic]_[Timestamp]`

### Example Command Line Usage

```bash
# Run with custom configuration
uvicorn research_and_analyst.api.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 📄 Sample Output

### Generated Report Structure

**File Location**: `generated_report/Impact_of_Generative_AI_on_jobs_20251110_162827/`

**Contents**:
- `Impact_of_Generative_AI_on_jobs_20251110_162827.pdf`
- `Impact_of_Generative_AI_on_jobs_20251110_162827.docx`

**Report Structure**:
1. **Title Page**: Topic and generation timestamp
2. **Introduction**: Overview and context setting
3. **Body Sections**: 
   - Multiple themed sections based on research
   - Each section derived from interview Q&A
   - Comprehensive coverage of topic
4. **Conclusion**: Key findings and synthesis
5. **Sources**: Referenced web sources from research

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Contributors

**Project Maintainer**: [Krishna Thakkar](https://github.com/Krishna-Thakkar)

Special thanks to all contributors who have helped shape this project!

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Krishna-Thakkar/automated-research-report-generation/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Krishna-Thakkar/automated-research-report-generation/discussions)

---

## 🌟 Acknowledgments

- Built with [LangGraph](https://langchain-ai.github.io/langgraph/) for workflow orchestration
- Powered by [FastAPI](https://fastapi.tiangolo.com/) for high-performance API
- Web research enabled by [Tavily](https://tavily.com/)
- AI capabilities provided by Google and Groq

---

<div align="center">

**Made with ❤️ by Krishna Thakkar**

If you find this project useful, please consider giving it a ⭐ on GitHub!

[Report Bug](https://github.com/Krishna-Thakkar/automated-research-report-generation/issues) · [Request Feature](https://github.com/Krishna-Thakkar/automated-research-report-generation/issues)

</div>