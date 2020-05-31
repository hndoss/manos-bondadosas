const Validator = {
    validateTextField(field, length) {
        return [
            text => !!text || `${field} is required`,
            text => (text && text.length <= length) || `${field} must be less than 10 characters`,
        ]

    },
    validateSelect(field) {
        return [
            text => !!text || `${field} is required`,
        ]
    },
    validateEmail() {
        return [
            email => !!email || 'E-mail is required',
            email => /.+@.+\..+/.test(email) || 'E-mail must be valid',
        ]
    }
}

export default Validator