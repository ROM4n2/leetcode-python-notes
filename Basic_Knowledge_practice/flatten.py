def flatten(nested_list):
    """
    将嵌套列表扁平化为一维列表

    参数:
        nested_list: 任意嵌套层次的列表

    返回:
        一维列表
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            # 递归展平子列表
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    # 示例用法
    data = [1, [2, [3, 4], 5], [6, 7], 8]
    flat = flatten(data)
    print(f"原始: {data}")
    print(f"扁平化: {flat}")
