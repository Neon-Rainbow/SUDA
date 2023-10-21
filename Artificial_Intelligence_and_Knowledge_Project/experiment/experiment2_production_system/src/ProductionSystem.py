import ProductionRule


class ProductionSystem:
    def __init__(self) -> None:
        """
        构造函数,构建一个空的产生式系统
        """
        self.rules_system = []

    def addRule(self, rule: ProductionRule) -> None:
        """
        该函数用于向产生式系统中增加一条规则
        :param rule: 新增的规则
        :return: None: 无返回值
        """
        self.rules_system.append(rule)

    def forwardChaining(self, facts: dict) -> set:
        """
        该函数用于正向推理,给定事实,然后进行正向推理,给出最终推理得到的结论
        :param facts: 给定的用于正向推理的事实,为dict类型,如同{"有奶": True, "有毛发": True},key为条件,value为真伪性
        :return: 最终返回正向推理得到的结论
        """
        conclusions: set = set()
        while True:
            new_conclusion: set = set()
            for rule in self.rules_system:
                current_action: str or None = rule.evaluate(facts)
                if current_action is not None and current_action not in facts:
                    new_conclusion.add(current_action)
            if not new_conclusion:
                break
            # 将集合转换为字典，以便将其添加到 facts 中
            new_facts = {key: True for key in new_conclusion}
            facts.update(new_facts)
            conclusions.update(new_conclusion)
        return conclusions

    def backwardChaining(self, facts: dict, goal: str) -> list or None:
        """
        该函数用于反向推理,给定事实facts,给定最终推导的目标goal来进行反向推理
        :param facts: dict,给定的事实集合,例如{"有奶": True, "有毛发": True},key为条件,value为该条件的真伪
        :param goal: str,给定的最终推导的目标
        :return: 若最终推导成功,则返回推导的路径;若推导不成功,则返回None
        """
        if goal in facts:
            return [goal]
        for rule in self.rules_system:
            current_action: str = rule.action
            if current_action == goal:
                new_facts = facts.copy()
                new_facts.update(rule.condition)
                if self.backwardChaining(new_facts, current_action):
                    return [current_action] + self.backwardChaining(new_facts, current_action)
        return None
