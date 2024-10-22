> Ilyas, A., Santurkar, S., Tsipras, D., Engstrom, L., Tran, B., & Madry, A. (2019). Adversarial examples are not bugs, they are features. Advances in neural information processing systems, 32. https://arxiv.org/pdf/1905.02175

*feature types*

- a) useless features
	- we assume that if a feature is useless, the neural net / feature extraction component will not pick up on it
- b) robust features
	- comprehensible to humans
	- remain stable under small perturbations
- c) non-robust features
	- learned by supervised learning algorithms
	- derived from patterns in the data distribution
	- very predictive but also brittle under small perturbations
	- incomprehensible to humans

*robust features model*

- the models' sensitivity to well-generalizing features is what causes adversarial vulnerability.
- adversarial vulnerability is a human-centric phenomenon, since from the algorithm's perspective non-robust features can be as important as robust ones.
- models built for interpretability / human-meaningful explainations aren't faithful to how the model was trained.

*adversarial transferability*

- = adversarial perturbations computed for one model often transfer to other, independently trained models
- this is because models learn similar non-robust features

*robust vs. non-robust datasets*

- standard accuracy = model's generalizability on the default test data
- robust accuracy = model's performance on adversarial examples
- **robust dataset** = training set without non-robust features
	- evaluation: good standard accuracy - bad robust accuracy
	- this is because adversarial vulnerability is a property of the dataset, not the algorithm (!!)
	- contains less information about the original dataset
- **non-robust dataset** = training set with perturbations
	- evaluation: good standard accuracy - bad robust accuracy (because they're sensitive to perturbations)
	- dataset gets labeled correctly by algorithm, but wrongly by human, meaning that it only contains non-robust features
	- means that adversarial perturbations can arise from flipping features in the data that are useful for classification of correct inputs
- **adversarial training** = mixing adversarial examples into train set
	- evaluation: good standard accuracy - good robust accuracy

note: to get the robust dataset you need to have a pretrained robust classifier. the robust classifier is obtained using adversarial training. so essentially this is transfer learning.

*misalignment*

- there is a misalignment between robustness (specified by humans) vs. the data geometry
- adversarial vulnerability is the difference between the data geometry and the perturbations

# questions

- what's the point of standard-training using $\hat{\mathcal{D}_{R}}$ when (1) you need a robustified model that has been created using adversarial-training in the first place and (2) adversarial-training using $\mathcal D$ itself has both higher standard accuracy and higher adversarial accuracy?
- it the robustness vs. accuracy trade-off real? the benchmark for the adversarial training seems to be only marginally less effective than standard training with unmodified $\mathcal D$.
- interesting youtube comment: I wonder if combining image pyramids with transformer networks would make the small features less useful than larger ones, or make them more independent, kind of like the "Processing Megapixel Images" paper. In the image pyramid case, larger features would show up somewhere in the most shrunken image, and several larger images, while smaller features would show up at the bottom and would be part of the larger features, but might not always. I think recognizing this way could improve recognizing drawings of cats after only seeing actual cats before.

# footnotes

paper reviews:

- https://www.youtube.com/watch?v=hMO6rbMAPew 🔥 (perfect explaination)
- https://www.youtube.com/watch?v=-vhUWSHOqIM

additional material:

- https://gradientscience.org/intro_adversarial/
- https://gradientscience.org/adv/
- https://distill.pub/2019/advex-bugs-discussion/ 🔥 (interesting discussions)
- https://github.com/MadryLab/constructed-datasets
