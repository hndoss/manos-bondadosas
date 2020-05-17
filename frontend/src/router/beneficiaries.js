import ListBeneficiaries from "@/pages/beneficiaries/listBeneficiaries"
import ShowBeneficiary from "@/pages/beneficiaries/showBeneficiary"

export default [
  {
    name: 'ListBeneficiaries',
    path: '/beneficiaries/',
    component: ListBeneficiaries,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: 'ShowBeneficiary',
    path: '/beneficiaries/:id',
    component: ShowBeneficiary,
    meta: {
      requiresAuth: true
    }
  }
]
