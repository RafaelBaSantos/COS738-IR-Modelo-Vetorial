def precision(tp, fp):
    if tp + fp == 0:
        return 0
    return tp / (tp + fp)


def eleven_point_interpolated_ap(gt_labels, pred_labels, num_classes):
    ap_sum = 0.0
    for c in range(num_classes):
        tp = 0
        fp = 0
        num_gt = sum([1 for l in gt_labels if l == c])
        if num_gt == 0:
            continue
        recall_step = 1.0 / 10
        precisions = []
        for r in range(11):
            threshold = r * recall_step
            tp += sum([1 for i in range(len(pred_labels)) if pred_labels[i] == c and gt_labels[i] == c and pred_labels[i] >= threshold])
            fp += sum([1 for i in range(len(pred_labels)) if pred_labels[i] == c and gt_labels[i] != c and pred_labels[i] >= threshold])
            precisions.append(precision(tp, fp))
        ap_sum += sum(precisions) / 11.0
    return ap_sum / num_classes


gt_labels = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1]
pred_labels = [0.3, 0.6, 0.8, 0.2, 0.7, 0.1, 0.4, 0.9, 0.5, 0.8]
num_classes = 2
ap = eleven_point_interpolated_ap(gt_labels, pred_labels, num_classes)
print(ap)
