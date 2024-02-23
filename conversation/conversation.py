
# conversation类用于管理人和AI之间整体的交流情况
class conversation:
    def __init__(self):
        self.chat_history = []

    def add_conversation(self, role, content, llm_mask=False):
        new_record = dict()
        new_record['role'] = role
        new_record['content'] = content
        new_record['llm_mask'] = llm_mask
        self.chat_history.append(new_record)

    def get_llm_input_format(self):
        llm_input = []
        for record in self.chat_history:
            if not record['llm_mask']:
                new_record = dict()
                new_record['role'] = record['role']
                new_record['content'] = record['content']
                llm_input.append(new_record)
        return llm_input
    