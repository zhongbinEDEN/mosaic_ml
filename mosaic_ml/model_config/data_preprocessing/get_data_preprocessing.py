from mosaic_ml.model_config.data_preprocessing import extra_trees_preproc_for_classification, kernel_pca, \
    kitchen_sinks, liblinear_svc_preprocessor, fast_ica, feature_agglomeration, nystroem_sampler, \
    pca, polynomial, random_trees_embedding, select_percentile_classification, select_rates, truncatedSVD

from mosaic_ml.model_config.data_preprocessing.densifier import Densifier


def evaluate(choice, config, random_state):
    from sklearn.preprocessing import FunctionTransformer

    if choice == "no_preprocessing":
        return (choice, FunctionTransformer())
    elif choice == "densifier":
        return (choice, Densifier())
    elif choice == "extra_trees_preproc_for_classification":
        return extra_trees_preproc_for_classification.get_model(choice, config, random_state)
    elif choice == "fast_ica":
        return fast_ica.get_model(choice, config, random_state)
    elif choice == "feature_agglomeration":
        return feature_agglomeration.get_model(choice, config, random_state)
    elif choice == "kernel_pca":
        return kernel_pca.get_model(choice, config, random_state)
    elif choice == "kitchen_sinks":
        return kitchen_sinks.get_model(choice, config, random_state)
    elif choice == "liblinear_svc_preprocessor":
        return liblinear_svc_preprocessor.get_model(choice, config, random_state)
    elif choice == "nystroem_sampler":
        return nystroem_sampler.get_model(choice, config, random_state)
    elif choice == "pca":
        return pca.get_model(choice, config, random_state)
    elif choice == "polynomial":
        return polynomial.get_model(choice, config, random_state)
    elif choice == "random_trees_embedding":
        return random_trees_embedding.get_model(choice, config, random_state)
    elif choice == "select_percentile_classification":
        return select_percentile_classification.get_model(choice, config, random_state)
    elif choice == "select_rates":
        return select_rates.get_model(choice, config, random_state)
    elif choice == "truncatedSVD":
        return truncatedSVD.get_model(choice, config, random_state)
    else:
        raise Exception("Data processing {0} not implemented".format(choice))
