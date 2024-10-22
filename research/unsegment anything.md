> Lu, J., Yang, X., & Wang, X. (2024). Unsegment Anything by Simulating Deformation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 24294-24304). https://arxiv.org/pdf/2404.02585

*SAM - segment anything model*

- promptable segmentation models
- generalize well, relatively robust
- generate a mask:
	- $M=g_{\theta^M}(f_{\theta^I}(I),h_{\theta^P}(P))$
	- $M$ = mask
	- $g_{\theta^M}(.)$ = mask decoder
	- $f_{\theta^I}(I)$ = image encoder
	- $h_{\theta^P}(P))$ = prompt encoder

*UAD attack - unsegment anything by simulating deformation*

- transferable adversarial attack on prompt-based segmentation models
	- prompt agnostic, model agnostic, highly transferable (existing solutions like attack-sam work well, but they aren't prompt-agnostic and only work on pixel-level classification)
- learnings:
	- prompt-specific attacks (ie. just thinking of common prompts and distorting the results) is prone to overfitting, doesn't generalize
	-  it's more common for models to share image encoders than prompt encoders or mask decoders - which is why image encoders are a better attack target
	- targeted feature perturbations are more transferable than untargeted ones
		- untargeted feature perturbation = maximize the distance between adversarial features and original features in the feature-space
		- targeted feature perturbation = bring adversarial sample closer to a specified input in the feature-space
- alters structural information through flow fields
- disrupts image encoder features

*UAD stage 1: deformation with flow fields*

- $\hat{I}^{*} = {\text{argmin}}_{\hat{I}}   \mathcal{L}_D+\lambda_C\mathcal{L}_C+\lambda_F\mathcal{L}_F$
- learn the optimal deformed target-image
- image-deformation-function can be learned through backprop because it's differentiable
- lambdas are coefficients of each loss term

where:

- $\hat{I}=\mathcal{D}_w(I)$
	- $\hat{I}$ = preturbed / deformed image
	- $w$ = flow field weights that define a delta for all coordinates in image $\hat{{I}}^{(i\boldsymbol{+}\Delta u^i,j\boldsymbol{+}\Delta v^j)}$ – but in theory any kind of deformation (ie. rotation, translation, scaling, warping) would have been fine
- $\mathcal{L}_D=SSIM(\hat{I},I)$
	- structural similairty index
	- zero loss is achieved quickly, even when there's still room for improvement
- $\mathcal{L}_C=\lambda_1\mathcal{L}_{TV}+\lambda_2\mathcal{L}_{var}$
	- control loss
	- total variation loss to regularize and promote: locally smooth spatial transformation, globally uniform deformation like shifting
	- creates effect of assembling wrapped and shifted images
- $\mathcal{L}_F(\hat{I},I+r^{\prime*})$
	- fidelity loss

*UAD stage 2: feature simulation*

- $r^*=\arg\min_r\mathcal{L}_F(\hat{I},I+r)-\mathcal{L}_F(I,I+r)$
- reduce the distance of the adversarial perturbation to learned target image
- increase the distance of the original image to the learned target image

*evaluation*

- measuring efficiency of attacks
- mean Intersection over Union (mIoU) = average attack performance (lower is better)
- attack success rate at IoU <50% (ASR@50) = number of destroyed output masks (higher is better)
- improvement over previous models, ie. ASR@50 at 69.95 (previously at 65.86)

# questions

- what do the authors mean by "we reveal that it is better to perturb features along the image manifold than against it to create a transferable adversarial sample" - which manifold? is this referring to the dimpled-manifold-model?

# footnotes

code:

- https://github.com/jiahaolu97/anything-unsegmentable
