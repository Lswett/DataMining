import numpy as np

def entropy(seniors, juniors):
    total = seniors + juniors
    if total == 0:
        return 0  # Avoid log(0)
    
    p_senior = seniors / total if seniors > 0 else 0
    p_junior = juniors / total if juniors > 0 else 0
    
    entropy_val = 0
    #print(entropy_val)
    if p_senior > 0:
        entropy_val -= p_senior * np.log2(p_senior)
        #print(entropy_val)
    if p_junior > 0:
        entropy_val -= p_junior * np.log2(p_junior)
        #print(entropy_val)
    return entropy_val

def calculate_information_gain(departments, senior_counts, junior_counts):
    # Compute total counts
    total_seniors = np.sum(senior_counts)
    total_juniors = np.sum(junior_counts)
    total = total_seniors + total_juniors
    
    # Compute Info(D)
    info_D = entropy(total_seniors, total_juniors)
    
    # Compute Info(department)
    info_department = 0
    for seniors, juniors in zip(senior_counts, junior_counts):
        total_dept = seniors + juniors
        info_department += (total_dept / total) * entropy(seniors, juniors)
    
    # Compute Information Gain
    information_gain = info_D - info_department
    
    return info_D, info_department, information_gain

# Example data
departments = ["sales", "systems", "marketing", "secretary"]
senior_counts = np.array([30, 8, 10, 4])
junior_counts = np.array([80, 23, 4, 6])

# Calculate results
info_D, info_department, info_gain = calculate_information_gain(departments, senior_counts, junior_counts)

# Print results
print(f"Info(D): {info_D:.4f}")
print(f"Info(department): {info_department:.4f}")
print(f"Information Gain: {info_gain:.4f}")