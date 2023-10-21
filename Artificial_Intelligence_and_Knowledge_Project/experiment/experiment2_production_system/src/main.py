import ProductionRule as pr
import ProductionSystem as ps

rules = [
    pr.ProductionRule({"有奶": True}, "哺乳动物"),
    pr.ProductionRule({"有毛发": True}, "哺乳动物"),
    pr.ProductionRule({"有羽毛": True}, "鸟"),
    pr.ProductionRule({"会飞": True, "生蛋": True}, "鸟"),
    pr.ProductionRule({"哺乳动物": True, "有爪": True, "有犬齿": True, "目盯前方": True}, "食肉动物"),
    pr.ProductionRule({"哺乳动物": True, "吃肉": True}, "食肉动物"),
    pr.ProductionRule({"哺乳动物": True, "有蹄": True}, "有蹄动物"),
    pr.ProductionRule({"有蹄动物": True, "反刍食物": True}, "偶蹄动物"),
    pr.ProductionRule({"食肉动物": True, "黄褐色": True, "有黑色条纹": True}, "老虎"),
    pr.ProductionRule({"食肉动物": True, "黄褐色": True, "有黑色斑点": True}, "金钱豹"),
    pr.ProductionRule({"有蹄动物": True, "长腿": True, "长脖子": True, "黄褐色": True, "有暗斑点": True}, "长颈鹿"),
    pr.ProductionRule({"有蹄动物": True, "白色": True, "有黑色条纹": True}, "斑马"),
    pr.ProductionRule({"鸟": True, "不会飞": True, "长腿": True, "长脖子": True, "黑白色": True}, "驼鸟"),
    pr.ProductionRule({"鸟": True, "不会飞": True, "会游泳": True, "黑白色": True}, "企鹅"),
    pr.ProductionRule({"鸟": True, "善飞": True, "不怕风浪": True}, "海燕"),
]

facts = {
    "有毛发": True,
    "吃肉": True,
    "黄褐色": True,
    "有黑色条纹": True
}

if __name__ == "__main__":
    system = ps.ProductionSystem()
    for rule in rules:
        system.addRule(rule)
    # 正向推理
    print(f"正向推理的结果是:{system.forwardChaining(facts)}")

    # 反向推理
    goal = "老虎"
    explanation = system.backwardChaining(facts, goal)
    if explanation:
        print("反向推理成功")
    else:
        print("反向推理不成功")
