


def father_status(obj):
    if obj.salary<5000:
            return "Poor"
    if obj.salary <20000:
            return "Middle class"
    return "rich"
    
    
def mother_status(obj):
    if obj.cash<500:
            return "Poor"
    if obj.cash <2000:
            return "Middle class"
    return "rich"