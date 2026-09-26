scenarios = [
    {
        "id": 1, "title": "THE IMPOSSIBLE CHOICE",
        "question": "Your teammate is trapped in a collapsing building while the rest of the team is evacuating. What do you do?",
        "options": {
            "A": {"text": "Go back immediately, even if it puts you at risk.", "traits": {"self_sacrifice":2,"loyalty":2,"risk_taking":1,"strategic_thinking":-1,"independence":-1}},
            "B": {"text": "Send another team member while you coordinate the evacuation.", "traits": {"leadership":2,"loyalty":1,"strategic_thinking":2,"risk_taking":-1,"impulsiveness":-1}},
            "C": {"text": "Analyze the building and calculate the safest rescue route.", "traits": {"strategic_thinking":2,"risk_taking":1,"independence":1,"empathy":-1,"loyalty":-1}},
            "D": {"text": "Continue the evacuation because saving the majority comes first.", "traits": {"moral_reasoning":2,"independence":1,"leadership":1,"self_sacrifice":-1,"empathy":-1}}
        }
    },
    {
        "id": 2, "title": "THE BETRAYAL",
        "question": "Someone you trusted has betrayed your team, but you discover they had a serious reason for doing it. What do you do?",
        "options": {
            "A": {"text": "Forgive them and try to understand their situation.", "traits": {"empathy":2,"loyalty":1,"moral_reasoning":1,"independence":-1,"risk_taking":-1}},
            "B": {"text": "Keep them under observation but give them another chance.", "traits": {"strategic_thinking":1,"loyalty":2,"empathy":1,"moral_reasoning":-1,"impulsiveness":-1}},
            "C": {"text": "Remove them from the team immediately.", "traits": {"independence":2,"leadership":1,"moral_reasoning":1,"empathy":-1,"loyalty":-1}},
            "D": {"text": "Confront them first and demand the complete truth.", "traits": {"risk_taking":1,"independence":1,"moral_reasoning":2,"loyalty":-1,"empathy":-1}}
        }
    },
    {
        "id": 3, "title": "UNDER PRESSURE",
        "question": "You have only 30 seconds to make a decision and your team is waiting for your command. What is your instinct?",
        "options": {
            "A": {"text": "Trust your instincts and act immediately.", "traits": {"impulsiveness":2,"risk_taking":2,"humor":1,"strategic_thinking":-1,"moral_reasoning":-1}},
            "B": {"text": "Quickly analyze the available information.", "traits": {"strategic_thinking":2,"independence":1,"humor":-1,"impulsiveness":-1}},
            "C": {"text": "Ask your team what they think before deciding.", "traits": {"leadership":1,"empathy":1,"loyalty":1,"independence":-1,"risk_taking":-1}},
            "D": {"text": "Make the safest decision even if it isn't popular.", "traits": {"independence":2,"moral_reasoning":1,"impulsiveness":-1,"empathy":-1}}
        }
    },
    {
        "id": 4, "title": "THE RISK",
        "question": "You discover technology that could save thousands, but there is a 40% chance it could make things worse. What do you do?",
        "options": {
            "A": {"text": "Use it. Someone has to take the risk.", "traits": {"risk_taking":2,"impulsiveness":1,"humor":1,"self_sacrifice":1,"moral_reasoning":-1,"strategic_thinking":-1}},
            "B": {"text": "Run simulations and find a safer way to use it.", "traits": {"strategic_thinking":2,"independence":1,"humor":-1,"risk_taking":-1}},
            "C": {"text": "Ask the team to vote on the decision.", "traits": {"leadership":1,"loyalty":1,"empathy":1,"humor":1,"independence":-1}},
            "D": {"text": "Destroy the technology because the risk is unacceptable.", "traits": {"moral_reasoning":2,"independence":1,"risk_taking":-1,"impulsiveness":-1}}
        }
    },
    {
        "id": 5, "title": "THE SACRIFICE",
        "question": "Your team can escape safely, but someone must stay behind to hold the enemy back. What do you do?",
        "options": {
            "A": {"text": "Volunteer yourself.", "traits": {"self_sacrifice":2,"loyalty":1,"risk_taking":1,"empathy":1,"strategic_thinking":-1,"independence":-1}},
            "B": {"text": "Find another solution so nobody has to stay.", "traits": {"strategic_thinking":2,"empathy":1,"humor":1,"risk_taking":-1,"impulsiveness":-1}},
            "C": {"text": "Choose the person most capable of handling it.", "traits": {"leadership":2,"strategic_thinking":1,"humor":-1,"empathy":-1,"risk_taking":-1}},
            "D": {"text": "Accept the sacrifice if it guarantees everyone else's survival.", "traits": {"moral_reasoning":2,"independence":1,"self_sacrifice":-1,"loyalty":-1}}
        }
    },
    {
        "id": 6, "title": "THE UNKNOWN PLAN",
        "question": "A mission is going wrong and your original plan no longer works. What is your first move?",
        "options": {
            "A": {"text": "Improvise immediately and trust your instincts.", "traits": {"impulsiveness":2,"risk_taking":1,"independence":1,"humor":1,"strategic_thinking":-1,"moral_reasoning":-1}},
            "B": {"text": "Pause and create a new strategy from available information.", "traits": {"strategic_thinking":2,"independence":1,"humor":-1,"impulsiveness":-1}},
            "C": {"text": "Keep the team calm and reorganize everyone's roles.", "traits": {"leadership":2,"empathy":1,"loyalty":1,"humor":-1,"independence":-1}},
            "D": {"text": "Protect the original objective no matter how difficult it becomes.", "traits": {"loyalty":2,"moral_reasoning":1,"strategic_thinking":-1,"impulsiveness":-1}}
        }
    },
    {
        "id": 7, "title": "THE STRANGER",
        "question": "A stranger asks your team for help, but helping could expose your own position. What do you do?",
        "options": {
            "A": {"text": "Help them because leaving someone behind feels wrong.", "traits": {"empathy":2,"self_sacrifice":1,"loyalty":1,"humor":-1,"independence":-1,"risk_taking":-1}},
            "B": {"text": "Check whether helping creates a manageable risk.", "traits": {"strategic_thinking":2,"risk_taking":-1,"impulsiveness":-1,"empathy":-1}},
            "C": {"text": "Ask your team to decide together.", "traits": {"loyalty":1,"leadership":1,"empathy":1,"humor":1,"independence":-1}},
            "D": {"text": "Stay focused on the mission and refuse.", "traits": {"independence":2,"moral_reasoning":1,"empathy":-1,"loyalty":-1}}
        }
    },
    {
        "id": 8, "title": "THE CHALLENGE",
        "question": "Someone publicly doubts your ability to solve a difficult problem. How do you react?",
        "options": {
            "A": {"text": "Turn it into a joke and keep working.", "traits": {"humor":2,"independence":1,"risk_taking":1,"moral_reasoning":-1,"strategic_thinking":-1}},
            "B": {"text": "Prove your point with a carefully planned solution.", "traits": {"strategic_thinking":2,"leadership":1,"humor":-1,"risk_taking":-1}},
            "C": {"text": "Ignore them and focus on the people who depend on you.", "traits": {"loyalty":1,"self_sacrifice":1,"independence":1,"humor":-1,"risk_taking":-1}},
            "D": {"text": "Challenge them back and act immediately.", "traits": {"risk_taking":1,"impulsiveness":2,"humor":1,"moral_reasoning":-1,"strategic_thinking":-1}}
        }
    },
    {
        "id": 9, "title": "THE TEAM",
        "question": "Your team has several talented people but everyone wants to lead. What do you do?",
        "options": {
            "A": {"text": "Take command and assign everyone a role.", "traits": {"leadership":2,"strategic_thinking":1,"independence":-1,"empathy":-1}},
            "B": {"text": "Find the person best suited to lead this mission.", "traits": {"strategic_thinking":2,"moral_reasoning":1,"leadership":-1,"humor":-1}},
            "C": {"text": "Let everyone contribute and build a shared plan.", "traits": {"empathy":1,"loyalty":2,"leadership":-1,"independence":-1,"risk_taking":-1}},
            "D": {"text": "Step back and work independently on the critical part.", "traits": {"independence":2,"strategic_thinking":1,"humor":1,"loyalty":-1,"empathy":-1}}
        }
    },
    {
        "id": 10, "title": "THE FINAL DECISION",
        "question": "You can achieve the mission, but only by making a choice that will personally cost you. What do you do?",
        "options": {
            "A": {"text": "Accept the cost if it protects everyone else.", "traits": {"self_sacrifice":2,"empathy":1,"loyalty":1,"independence":-1,"risk_taking":-1}},
            "B": {"text": "Search for a third option before accepting the cost.", "traits": {"strategic_thinking":2,"independence":1,"self_sacrifice":-1,"risk_taking":-1,"humor":1}},
            "C": {"text": "Make the choice that follows your principles.", "traits": {"moral_reasoning":2,"independence":1,"humor":-1,"impulsiveness":-1}},
            "D": {"text": "Take the leap and deal with the consequences later.", "traits": {"risk_taking":2,"impulsiveness":1,"humor":1,"moral_reasoning":-1,"strategic_thinking":-1}}
        }
    }
]
