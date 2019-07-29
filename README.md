# InstaBoost

A python implementation for paper: "**InstaBoost: Boosting Instance Segmentation Via Probability Map Guided Copy-Pasting**"

## Install

**pip install InstaBoost**

Only test on python3

## Get Started

There are two main interface in **InstaBoost**.

```
cfg = InstaBoostConfig(action_candidate: tuple,
                       action_prob: tuple, 
                       scale: tuple, 
                       dx: float, 
                       dy: float,
                       theta: tuple, 
                       color_prob: float, 
                       heatmap_flag: bool)
```
**action_candidate:** tuple of action candidates. 'normal', 'horizontal', 'vertical', 'skip' are supported

**action_prob:** tuple of corresponding action probabilities. Should be the same length as action_candidate

**scale:** tuple of (min scale, max scale)

**dx:** the maximum x-axis shift will be  (instance width) / dx

**dy:** the maximum y-axis shift will be  (instance height) / dy

**theta:** tuple of (min rotation degree, max rotation degree)

**color_prob:** the probability of images for color augmentation

**heatmap_flag:** whether to use heatmap guided

```
new_ann, new_img = get_new_data(ori_anns: list, 
                                ori_img: np.ndarray, 
                                config: InstaBoostConfig, 
                                background: np.ndarray)
```

**ori_anns:** list of coco-style annotation dicts

**ori_img:** images corresponding to ori_anns

**config:** a InstaBoostConfig instance. If None, the default parameters will be used

**background:** if not None, this background image will be used for augmentation
