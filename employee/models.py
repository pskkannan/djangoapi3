from mongoengine import Document, EmbeddedDocument, fields


class Projects(EmbeddedDocument):
    projectId = fields.StringField(max_length=10, required=True, null=False)
    projectName = fields.StringField(max_length=50, required=True, null=False)
    startDate = fields.DateTimeField()
    endDate = fields.DateTimeField()


class Skills(EmbeddedDocument):
    technology = fields.StringField(max_length=100, required=True, null=False)
    experience = fields.IntField()
    level = fields.IntField()


class Employee(Document):
    employeeId = fields.StringField(max_length=10, required=True, null=False)
    employeeName = fields.StringField(max_length=50, required=True)
    worklocation = fields.StringField(max_length=50, required=False)
    projects = fields.EmbeddedDocumentListField(Projects)
    skills = fields.EmbeddedDocumentListField(Skills)

