import ListBeneficiaries from "@/pages/beneficiaries/listBeneficiaries"
import ShowBeneficiary from "@/pages/beneficiaries/showBeneficiary"
import AddBeneficiary from "@/pages/beneficiaries/addBeneficiary"

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
  },
  {
    name: 'AddBeneficiary',
    path: '/add-beneficiary',
    component: AddBeneficiary,
    meta: {
      requiresAuth: true
    }
  }
]
