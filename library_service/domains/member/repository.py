class MemberRepository:
    def __init__(self):
        self.members = {}

    def add(self, member):
        self.members[member.member_id] = member

    def find_by_id(self, member_id):
        return self.members.get(member_id)
