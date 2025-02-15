import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data
nltk.download('punkt')

# Define syllabus details and exam preparation tips
syllabus = {
    "1st_semester": {
        "Theory_Subjects": [
            {"name": "IP3151 Induction Programme", "exam_tips": "Focus on understanding the induction program goals and participate actively in activities."},
            {"name": "HS3151 Professional English – I", "exam_tips": "Practice writing essays and improve your grammar. Review vocabulary and comprehension skills."},
            {"name": "MA3151 Matrices and Calculus", "exam_tips": "Solve previous years' question papers and focus on understanding concepts and problem-solving techniques."},
            {"name": "PH3151 Engineering Physics", "exam_tips": "Revise key formulas and concepts. Practice numerical problems and understand theoretical concepts."},
            {"name": "CY3151 Engineering Chemistry", "exam_tips": "Review chemical reactions and equations. Understand the periodic table and solve numerical problems."},
            {"name": "GE3151 Problem Solving and Python Programming", "exam_tips": "Practice coding regularly. Understand algorithms and data structures. Solve coding problems on platforms like LeetCode or HackerRank."},
            {"name": "GE3152 Heritage of Tamils", "exam_tips": "Read about Tamil heritage and culture. Focus on historical events and their significance."}
        ],
        "Practical_Subjects": [
            {"name": "GE3171 Problem Solving and Python Programming Laboratory", "exam_tips": "Practice coding and debugging. Understand the practical applications of programming concepts."},
            {"name": "BS3171 Physics and Chemistry Laboratory", "exam_tips": "Review laboratory experiments and understand the principles behind them. Practice writing lab reports."},
            {"name": "GE3172 English Laboratory", "exam_tips": "Practice speaking and listening skills. Participate in language activities and exercises."}
        ]
    },
    "2nd_semester": {
        "Theory_Subjects": [
            {"name": "HS3252 Professional English – II", "exam_tips": "Continue practicing writing and comprehension skills. Participate in group discussions and presentations."},
            {"name": "MA3251 Statistics and Numerical Methods", "exam_tips": "Solve statistical problems and numerical methods exercises. Understand key concepts and formulas."},
            {"name": "PH3251 Materials Science", "exam_tips": "Review materials properties and applications. Understand the structure and behavior of different materials."},
            {"name": "BE3251 Basic Electrical and Electronics Engineering", "exam_tips": "Revise electrical circuits and electronics fundamentals. Practice solving circuit problems."},
            {"name": "GE3251 Engineering Graphics", "exam_tips": "Practice drawing and interpreting engineering diagrams. Understand projection techniques."},
            {"name": "GE3252 தமிழ் தொழில்நுட்பம் / Tamils and Technology", "exam_tips": "Read about Tamil technology and advancements. Focus on historical and modern applications."}
        ],
        "Practical_Subjects": [
            {"name": "GE3271 Engineering Practices Laboratory", "exam_tips": "Gain hands-on experience with engineering practices. Understand the principles behind each experiment."},
            {"name": "GE3272 English Laboratory", "exam_tips": "Continue improving language skills through practical exercises. Participate in speaking and listening activities."},
            {"name": "BS3271 Physics and Chemistry Laboratory", "exam_tips": "Review and understand the experiments conducted. Practice writing detailed lab reports."}
        ]
    },
    "3rd_semester": {
        "Theory_Subjects": [
            {"name": "MA3354 Discrete Mathematics", "exam_tips": "Understand set theory, algebra, and graph theory concepts. Solve problems regularly."},
            {"name": "CS3351 Digital Principles and Computer Organization", "exam_tips": "Review digital logic and computer architecture. Practice solving design problems."},
            {"name": "AD3391 Database Design and Management", "exam_tips": "Understand database concepts and data modeling. Practice designing and managing databases."},
            {"name": "AD3351 Design and Analysis of Algorithms", "exam_tips": "Focus on algorithm design and analysis. Solve problems on algorithm complexity and optimization."},
            {"name": "AD3301 Data Exploration and Visualization", "exam_tips": "Understand data visualization techniques. Practice creating visualizations using tools like Tableau."},
            {"name": "AL3391 Artificial Intelligence", "exam_tips": "Review AI concepts and machine learning techniques. Practice implementing AI algorithms."}
        ],
        "Practical_Subjects": [
            {"name": "AD3381 Database Design and Management Laboratory", "exam_tips": "Gain hands-on experience with database design and management tools. Practice writing SQL queries."},
            {"name": "AD3311 Artificial Intelligence Laboratory", "exam_tips": "Implement AI algorithms in practice. Understand the practical applications of AI concepts."},
            {"name": "GE3361 Professional Development", "exam_tips": "Focus on developing professional skills, communication, and teamwork. Participate in workshops and activities."}
        ]
    },
    "4th_semester": {
        "Theory_Subjects": [
            {"name": "CS3451 Computer Networks", "exam_tips": "Understand network protocols and architecture. Practice solving network design problems."},
            {"name": "AD3491 Machine Learning", "exam_tips": "Focus on machine learning algorithms and applications. Practice implementing algorithms in Python."},
            {"name": "AD3401 Data Mining and Warehousing", "exam_tips": "Review data mining techniques and warehousing concepts. Practice using data mining tools."},
            {"name": "AD3451 Human-Computer Interaction", "exam_tips": "Understand HCI principles and design. Practice evaluating human-computer interfaces."},
            {"name": "AD3492 Deep Learning", "exam_tips": "Review deep learning architectures and applications. Practice implementing deep learning models."},
            {"name": "AL3491 Natural Language Processing", "exam_tips": "Focus on NLP techniques and applications. Practice using NLP libraries like spaCy and NLTK."}
        ],
        "Practical_Subjects": [
            {"name": "AD3481 Machine Learning Laboratory", "exam_tips": "Gain hands-on experience with machine learning tools. Practice implementing algorithms and analyzing results."},
            {"name": "AD3411 Data Mining and Warehousing Laboratory", "exam_tips": "Practice using data mining and warehousing tools. Understand the practical applications of concepts."},
            {"name": "AD3461 Human-Computer Interaction Laboratory", "exam_tips": "Focus on designing and evaluating human-computer interfaces. Participate in usability testing activities."}
        ],
        "Elective_Subject": [
            {"name": "AD3493 Special Topic in AI and DS", "exam_tips": "Review advanced topics in AI and DS. Participate in discussions and research activities."}
        ]
    },
    "5th_semester": {
        "Theory_Subjects": [
            {"name": "CS3551 Operating Systems", "exam_tips": "Understand OS concepts, process management, and memory management. Practice solving OS-related problems."},
            {"name": "AD3591 Computer Vision", "exam_tips": "Focus on computer vision algorithms and applications. Practice implementing vision algorithms in Python."},
            {"name": "AD3501 Web Technology and Development", "exam_tips": "Understand web development concepts. Practice building web applications using HTML, CSS, and JavaScript."},
            {"name": "AD3551 Data Science and Analytics", "exam_tips": "Review data science concepts and techniques. Practice data analysis and visualization using tools like Python and R."},
            {"name": "AD3592 Robotics and Intelligent Systems", "exam_tips": "Understand robotics concepts and intelligent systems. Practice solving robotics problems and implementing algorithms."}
        ],
        "Practical_Subjects": [
            {"name": "AD3581 Computer Vision Laboratory", "exam_tips": "Gain hands-on experience with computer vision tools. Practice implementing and testing vision algorithms."},
            {"name": "AD3511 Web Technology and Development Laboratory", "exam_tips": "Build and deploy web applications. Practice using web development frameworks and tools."},
            {"name": "AD3561 Data Science and Analytics Laboratory", "exam_tips": "Focus on data analysis and visualization. Practice using data science tools like Python, R, and Tableau."}
        ],
        "Elective_Subject": [
            {"name": "AD3593 Special Topic in AI and DS", "exam_tips": "Review advanced topics in AI and DS. Participate in discussions and research activities."}
        ]
    },
        "6th_semester": {
        "Theory_Subjects": [
            {"name": "AD3691 Expert Systems and Knowledge Engineering", "exam_tips": "Understand expert systems concepts and knowledge engineering techniques. Practice designing expert systems."},
            {"name": "AD3601 Internet of Things (IoT)", "exam_tips": "Focus on IoT architectures, protocols, and applications. Practice working with IoT devices and sensors."},
            {"name": "AD3651 Cognitive Computing", "exam_tips": "Review cognitive computing concepts and natural language processing techniques. Practice implementing cognitive computing models."},
            {"name": "AD3692 Blockchain Technology", "exam_tips": "Understand blockchain concepts, architectures, and applications. Review key blockchain technologies and platforms."},
            {"name": "AD3602 Geographical Information System (GIS)", "exam_tips": "Focus on GIS concepts and spatial data analysis. Practice using GIS tools and creating visualizations."}
        ],
        "Practical_Subjects": [
            {"name": "AD3681 Expert Systems and Knowledge Engineering Laboratory", "exam_tips": "Gain hands-on experience with expert systems and knowledge engineering tools. Practice designing and testing systems."},
            {"name": "AD3611 Internet of Things (IoT) Laboratory", "exam_tips": "Practice working with IoT devices, protocols, and applications. Understand the practical aspects of IoT implementations."},
            {"name": "AD3661 Cognitive Computing Laboratory", "exam_tips": "Focus on implementing cognitive computing models and applications. Practice using tools like Python and R."}
        ],
        "Elective_Subject": [
            {"name": "AD3693 Special Topic in AI and DS", "exam_tips": "Review advanced topics in AI and DS. Participate in discussions and research activities."}
        ],
        "Project_Subject": [
            {"name": "AD3671 Project Work", "exam_tips": "Work on a project related to AI and DS under the guidance of a faculty member. Focus on practical applications and research."}
        ]
    },
    "7th_semester": {
        "Theory_Subjects": [
            {"name": "AD3791 Advanced Machine Learning", "exam_tips": "Focus on advanced machine learning concepts, deep learning, and reinforcement learning. Practice implementing algorithms and models."},
            {"name": "AD3701 Human-Computer Interaction for AI Systems", "exam_tips": "Understand HCI principles and design for AI systems. Practice evaluating and improving AI interfaces."},
            {"name": "AD3751 Business Intelligence and Data Analytics", "exam_tips": "Review business intelligence concepts and data analytics techniques. Practice using tools like Tableau and Power BI."},
            {"name": "AD3792 Cyber-Physical Systems", "exam_tips": "Focus on cyber-physical systems, IoT, and smart systems. Understand the integration of physical and digital components."},
            {"name": "AD3702 Entrepreneurship and Innovation", "exam_tips": "Review entrepreneurship principles and the startup ecosystem. Participate in innovation activities and case studies."}
        ],
        "Practical_Subjects": [
            {"name": "AD3781 Advanced Machine Learning Laboratory", "exam_tips": "Gain hands-on experience with advanced machine learning tools and algorithms. Practice implementing and testing models."},
            {"name": "AD3711 Human-Computer Interaction Laboratory", "exam_tips": "Focus on designing and evaluating AI interfaces. Participate in usability testing and interface improvements."},
            {"name": "AD3761 Business Intelligence and Data Analytics Laboratory", "exam_tips": "Practice using business intelligence and data analytics tools. Understand practical applications and data visualization."}
        ],
        "Elective_Subject": [
            {"name": "AD3793 Special Topic in AI and DS", "exam_tips": "Review advanced topics in AI and DS. Participate in discussions and research activities."}
        ],
        "Project_Subject": [
            {"name": "AD3771 Project Work", "exam_tips": "Work on a project related to AI and DS under the guidance of a faculty member. Focus on practical applications and research."}
        ]
    },
    "8th_semester": {
        "Theory_Subjects": [
            {"name": "AD3891 Advanced Deep Learning", "exam_tips": "Focus on advanced deep learning concepts, architectures, and applications. Practice implementing deep learning models."},
            {"name": "AD3801 AI for Social Good", "exam_tips": "Review AI applications for social good, ethics, and fairness. Participate in discussions on ethical AI practices."},
            {"name": "AD3851 Data-Driven Decision Making", "exam_tips": "Understand data-driven decision-making concepts and business analytics. Practice using tools like Excel and Tableau."},
            {"name": "AD3892 Digital Twin", "exam_tips": "Focus on digital twin concepts, technologies, and applications. Practice designing and implementing digital twins."}
        ],
        "Practical_Subjects": [
            {"name": "AD3881 Advanced Deep Learning Laboratory", "exam_tips": "Gain hands-on experience with advanced deep learning tools and algorithms. Practice implementing and testing models."},
            {"name": "AD3811 AI for Social Good Laboratory", "exam_tips": "Focus on practical applications of AI for social good. Participate in projects and research activities."},
            {"name": "AD3861 Data-Driven Decision Making Laboratory", "exam_tips": "Practice using data-driven decision-making tools and techniques. Understand practical applications and business analytics."}
        ],
        "Elective_Subject": [
            {"name": "AD3893 Special Topic in AI and DS", "exam_tips": "Review advanced topics in AI and DS. Participate in discussions and research activities."}
        ],
        "Project_Subject": [
            {"name": "AD3871 Project Work", "exam_tips": "Work on a project related to AI and DS under the guidance of a faculty member. Focus on practical applications and research."}
        ]
    }
}

# Define a function to handle user queries
def handle_query(user_query):
    # Sample error handling: check if user_query is empty
    if not user_query:
        return "Please enter a valid query."

    # Use NLTK to process the user query
    tokens = word_tokenize(user_query.lower())

    semester = None
    subject_type = None

    # Extract semester and subject type from user query
    for token in tokens:
        if "1st" in token:
            semester = "1st_semester"
        elif "2nd" in token:
            semester = "2nd_semester"
        elif "3rd" in token:
            semester = "3rd_semester"
        elif "4th" in token:
            semester = "4th_semester"
        elif "5th" in token:
            semester = "5th_semester"
        elif "6th" in token:
            semester = "6th_semester"
        elif "7th" in token:
            semester = "7th_semester"
        elif "8th" in token:
            semester = "8th_semester"

        if "theory" in token:
            subject_type = "Theory_Subjects"
        elif "practical" in token:
            subject_type = "Practical_Subjects"
        elif "exam tips" in token:
            subject_type = "Exam_Tips"
        elif "elective" in token:
            subject_type = "Elective_Subject"
        elif "project" in token:
            subject_type = "Project_Subject"

    if not semester:
        return "Semester not found. Please specify a valid semester."

    if not subject_type:
        return "Subject type not found. Please specify 'theory', 'practical', 'exam tips', 'elective', or 'project' subjects."

    # Retrieve the syllabus details or exam tips
    try:
        subjects = syllabus[semester][subject_type]
        if subject_type == "Exam_Tips":
            response = f"Exam tips for {semester.replace('_', ' ').title()} are:\n"
            for subject in subjects:
                response += f"{subject['name']}: {subject['exam_tips']}\n"
        else:
            response = f"The {subject_type.replace('_', ' ').title()} for {semester.replace('_', ' ').title()} are:\n"
            for subject in subjects:
                response += subject['name'] + "\n"
        return response
    except KeyError:
        return "Invalid query. Please check the semester and subject type."

# Streamlit interface
st.title('University Syllabus Chatbot')

user_query = st.text_input('Enter your query:')
if st.button('Submit'):
    response = handle_query(user_query)
    st.text_area('Response:', value=response, height=300)