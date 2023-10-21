class ProductionRule:
    def __init__(self, condition: dict, action: str) -> None:
        """
        构造函数,用于构造一个规则
        :param condition:规则的前提条件,即 IF 语句中的条件,类型是字典,key为条件,value为条件的真假
        :param action:规则的结论,即通过前提条件可以推导得到的东西, THEN 语句中的内容
        :return None
        """
        self.condition: dict = condition
        self.action: str = action

    def evaluate(self, facts: dict) -> str or None:
        """
        该函数判断该规则是否可以与给定的事实匹配
        :param facts:给出的事实
        :return: str or None:如果该规则与给定的事实相匹配,则返回推导出的结论self.action,不然返回None
        """
        # 初始化一个列表来存储匹配的条件
        matching_conditions = []

        # 遍历规则的前提条件
        for rule_condition, rule_value in self.condition.items():
            # 检查是否存在相应的事实键，并检查其值是否与规则匹配
            if rule_condition in facts and facts[rule_condition] == rule_value:
                matching_conditions.append(True)
            else:
                matching_conditions.append(False)

        # 如果所有前提条件都匹配，返回结论，否则返回None
        if all(matching_conditions):
            return self.action
        else:
            return None
