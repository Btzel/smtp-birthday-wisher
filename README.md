# SMTP Birthday Wisher
Automated birthday email sender built with Python using SMTP and Pandas, featuring customizable templates and scheduled sending.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![SMTP](https://img.shields.io/badge/SMTP-Email-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data-red)
![Automation](https://img.shields.io/badge/Task-Automation-green)

## 🎯 Overview
This project creates an automated system that:
1. Checks daily for birthdays (if uploaded to cloud)
2. Selects random letter templates
3. Personalizes messages
4. Sends automated emails
5. Manages recipient data

## 🎮 Application Features
### Automation Elements
- Daily birthday checking
- Template randomization
- Email personalization
- SMTP integration
- CSV data management

### Data Processing
- Birthday verification
- Template selection
- Name replacement
- Email dispatch
- Success logging

## 🔧 Technical Components
### Email Processing System
```python
def prepare_letters(self):
    for person in self.birthday_persons:
        letter_file = open(f"./letter_templates/letter_{random.randint(1, 3)}.txt")
        person['letter'] = letter_file.read().replace("[NAME]", f"{person['name']}")
        letter_file.close()
```

### Key Features
1. **Birthday Detection**
   - Date comparison
   - CSV data reading
   - Daily checks
   - Multiple recipients

2. **Letter Management**
   - Template selection
   - Name personalization
   - Content customization
   - File handling

3. **Email System**
   - SMTP connection
   - Secure sending
   - Batch processing
   - Success verification

## 💻 Implementation Details
### Class Structure
- `LetterPreparer`: Birthday checking and letter preparation
- `MailSender`: Email dispatch system
- CSV-based contact management

### Data Management
- Contact information storage
- Template organization
- Email credentials
- Success logging

## 🚀 Usage
1. Install required packages:
```bash
pip install pandas
```

2. Configure the system:
   - Add SMTP credentials
   - Update email templates
   - Fill birthdays.csv
   - Set up automation by running in server daily

3. Run the application:
```bash
python main.py
```

## 🎯 System Rules
1. Store contacts in CSV format
2. Create email templates
3. Configure SMTP settings
4. Maintain valid email credentials
5. Schedule daily execution

## 🛠️ Project Structure
```
birthday-wisher/
├── main.py            # Main execution
├── letter_preparer.py # Birthday checking
├── mail_sender.py     # Email dispatch
├── birthdays.csv      # Contact database
└── letter_templates/  # Email templates
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt
```

## 📊 Features
### Input Requirements
- Contact information
- Email templates
- SMTP credentials
- Valid permissions

### Output Management
- Personalized emails
- Success logging
- Error handling
- Delivery confirmation

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL