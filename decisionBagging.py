import run_variants
import validation

#reading the training data


run_variants.decisionTrees(10)

## reading the training the data


# # #DECISION TREES WITH SVM
 

# n_svm_dt = validation.crossvalidation_svm_dt()
# print "Best gamma value is %s and C is %s"%(n_svm_dt[:n_svm_dt.index(" ")],n_svm_dt[n_svm_dt.index(" ")+1:])
# n_svm_n_dt = float(n_svm_dt[:n_svm_dt.index(" ")])
# n_svm_m_dt = float(n_svm_dt[n_svm_dt.index(" ")+1:])
# run_variants.svm_dt(n_svm_n_dt,n_svm_m_dt)















    



