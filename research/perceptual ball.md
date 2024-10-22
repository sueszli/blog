> Elliott, A., Law, S., & Russell, C. (2021). Explaining classifiers using adversarial perturbations on the perceptual ball. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 10693-10702). https://openaccess.thecvf.com/content/CVPR2021/papers/Elliott_Explaining_Classifiers_Using_Adversarial_Perturbations_on_the_Perceptual_Ball_CVPR_2021_paper.pdf

counterfactual explainations = answering the question "What is a minimal change that would result in a different outcome?" in the form "If X had not occurred, Y would not have occurred".

when we apply them to classifiers we essentially get "adversarial perturbations" - but can't use them for improved explainability because they aren't perceptible to the human eye and don't localize on objects.

if they were perceptible they would lie on the manifold of natural images and be larger.

they probably exist because of the exploding gradients phenomenon. we can avoid that exploit.

we can regularize/penalize them in a way that makes them perceivable by highlighting objects and regions of interest within the image.

this regularization is equivalent to staying within a ball defined by some $\rho$ while optimizing the loss function $\mathcal L$.

this makes the perturbations more meaningful and local to specific regions while still imperceptible to human eyes (it's still unknown why).

# footnotes

code: https://github.com/alan-turing-institute/perceptualBall
