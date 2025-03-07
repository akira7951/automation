from typing import Optional, Dict, Type, TypeVar, List

from pydantic import BaseModel, Field


class Event(BaseModel):
    version: int
    event: str
    type: str


class AccessGrantedEvent(Event):
    aid: Optional[str]
    expires: Optional[int]
    term_id: Optional[str]
    uid: Optional[str]
    rid: Optional[str]
    access_id: Optional[str]
    user_email: Optional[str]
    contract_id: Optional[str]
    payment_id: Optional[str]
    conversion_id: Optional[str]


class AccessModifiedEvent(Event):
    aid: Optional[str]
    expires: Optional[int]
    term_id: Optional[str]
    uid: Optional[str]
    rid: Optional[str]
    access_id: Optional[str]
    user_email: Optional[str]
    contract_id: Optional[str]
    payment_id: Optional[str]
    conversion_id: Optional[str]


class AccessRevokedEvent(Event):
    aid: Optional[str]
    expires: Optional[int]
    term_id: Optional[str]
    uid: Optional[str]
    rid: Optional[str]
    access_id: Optional[str]
    user_email: Optional[str]
    contract_id: Optional[str]


class AddressUpdatedEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    address_id: Optional[str]
    subscription_id: Optional[List[str]]
    voucher_id: Optional[List[str]]


class ContractCreatedEvent(Event):
    aid: Optional[str]
    contract_id: Optional[str]
    rid: Optional[str]
    term_id: Optional[str]


class ContractDeletedEvent(Event):
    aid: Optional[str]
    contract_id: Optional[str]
    rid: Optional[str]
    term_id: Optional[str]


class ContractRedeemedEvent(Event):
    aid: Optional[str]
    contract_id: Optional[str]
    rid: Optional[str]
    term_id: Optional[str]
    conversion_id: Optional[str]
    uid: Optional[str]
    user_email: Optional[str]
    expires: Optional[int]
    access_id: Optional[str]


class ContractRenewedEvent(Event):
    aid: Optional[str]
    contract_id: Optional[str]
    rid: Optional[str]
    term_id: Optional[str]
    conversion_id: Optional[str]
    uid: Optional[str]
    user_email: Optional[str]
    expires: Optional[int]
    access_id: Optional[str]


class ContractUpdatedEvent(Event):
    aid: Optional[str]
    contract_id: Optional[str]
    rid: Optional[str]
    term_id: Optional[str]


class ContractUserAccessExpiredEvent(Event):
    aid: Optional[str]
    contract_id: Optional[str]
    rid: Optional[str]
    term_id: Optional[str]
    uid: Optional[str]
    user_email: Optional[str]


class ContractUserAccessRevokedEvent(Event):
    aid: Optional[str]
    contract_id: Optional[str]
    rid: Optional[str]
    term_id: Optional[str]
    uid: Optional[str]
    user_email: Optional[str]


class ContractUserCreatedEvent(Event):
    aid: Optional[str]
    contract_id: Optional[str]
    rid: Optional[str]
    term_id: Optional[str]
    user_email: Optional[str]


class ContractUserInvitedEvent(Event):
    aid: Optional[str]
    contract_id: Optional[str]
    rid: Optional[str]
    term_id: Optional[str]
    user_email: Optional[str]


class KeyingEvent(Event):
    aid: Optional[str]
    timestamp: Optional[int]
    content_id: Optional[str]


class LicenseeCreatedEvent(Event):
    aid: Optional[str]
    licensee_id: Optional[str]


class LicenseeUpdatedEvent(Event):
    aid: Optional[str]
    licensee_id: Optional[str]


class PaymentRefundEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    payment_id: Optional[str]
    amount: Optional[float]
    subscription_id: Optional[str]
    access_id: Optional[str]


class SharedSubscriptionChildAccessGrantedEvent(Event):
    aid: Optional[str]
    expires: Optional[int]
    email: Optional[str]
    term_id: Optional[str]
    uid: Optional[str]
    rid: Optional[str]
    access_id: Optional[str]
    user_email: Optional[str]
    contract_id: Optional[str]
    payment_id: Optional[str]
    conversion_id: Optional[str]
    parent_uid: Optional[str]
    parent_subscription_id: Optional[str]


class SubscriptionAutoRenewChangedByEndUserEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    subscription_id: Optional[str]
    term_id: Optional[str]
    auto_renew: Optional[str]


class SubscriptionRenewalEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    rid: Optional[str]
    subscription_id: Optional[str]
    status: Optional[str]
    billing_plan: Optional[str]
    start_date: Optional[int]
    next_bill_date: Optional[int]
    term_id: Optional[str]
    term_type: Optional[str]
    access_id: Optional[str]
    user_email: Optional[str]
    upi_id: Optional[str]
    auto_renew: Optional[bool]
    is_in_grace: Optional[bool]
    grace_period_start_date: Optional[int]
    grace_period_length: Optional[int]
    failure_counter: Optional[int]
    passive_churn_logic_id: Optional[str]
    decline_reason: Optional[str]
    payment_id: Optional[str]
    renewed_by: Optional[str]


class TermChangeEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    user_email: Optional[str]
    previous_term_id: Optional[str]
    previous_term_name: Optional[str]
    new_term_id: Optional[str]
    new_term_name: Optional[str]
    previous_subscription_id: Optional[str]
    new_subscription_id: Optional[str]
    new_subscription_rid: Optional[str]
    new_subscription_access_id: Optional[str]
    new_billing_plan: Optional[str]
    new_subscription_next_bill_date: Optional[int]
    date_of_access_change: Optional[int]
    date_of_billing_change: Optional[int]
    upi_id: Optional[str]
    is_in_grace: Optional[bool]
    grace_period_start_date: Optional[int]
    grace_period_length: Optional[int]
    failure_counter: Optional[int]
    passive_churn_logic_id: Optional[str]
    decline_reason: Optional[str]
    payment_id: Optional[str]
    changed_by: Optional[str]


class TermChangeFinishedEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    previous_term_id: Optional[str]
    previous_term_name: Optional[str]
    new_term_id: Optional[str]
    new_term_name: Optional[str]
    previous_subscription_id: Optional[str]
    new_subscription_id: Optional[str]
    date_of_access_change: Optional[int]
    date_of_billing_change: Optional[int]
    new_billing_plan: Optional[str]


class TermChangedEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    previous_term_id: Optional[str]
    previous_term_name: Optional[str]
    new_term_id: Optional[str]
    new_term_name: Optional[str]
    previous_subscription_id: Optional[str]
    new_subscription_id: Optional[str]
    date_of_access_change: Optional[int]
    date_of_billing_change: Optional[int]
    new_billing_plan: Optional[str]


class TestEvent(Event):
    aid: Optional[str]
    timestamp: Optional[int]


class UnknownEvent(Event):
    pass


class UnsupportedEvent(Event):
    pass


class UserAddressUpdatedEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    term_id: Optional[str]
    sub_id: Optional[str]
    subscription_id: Optional[str]
    access_id: Optional[str]
    psc_subscriber_number: Optional[str]


class UserCreatedEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    timestamp: Optional[str]


class UserDisabledEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    timestamp: Optional[str]


class UserEmailConfirmedEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    timestamp: Optional[str]


class UserPaymentMethodEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    user_payment_info_id: Optional[str]
    user_subscriptions: Optional[List[str]]


class UserUpdatedEvent(Event):
    aid: Optional[str]
    uid: Optional[str]
    timestamp: Optional[str]
    updated_custom_fields: Optional[str]


class VoucherDeliveredEvent(Event):
    aid: Optional[str]
    voucher_id: Optional[str]
    voucher_state: Optional[int]
    voucher_send_date_timestamp: Optional[int]
    voucher_recipient_name: Optional[str]
    voucher_recipient_email: Optional[str]
    voucher_message: Optional[str]
    voucher_code: Optional[str]
    voucher_expires_timestamp: Optional[int]
    voucher_issue_term_conversion_id: Optional[str]
    voucher_redeem_term_conversion_id: Optional[str]
    term_id: Optional[str]
    address_id: Optional[str]


class VoucherPurchasedEvent(Event):
    aid: Optional[str]
    voucher_id: Optional[str]
    voucher_state: Optional[int]
    voucher_send_date_timestamp: Optional[int]
    voucher_recipient_name: Optional[str]
    voucher_recipient_email: Optional[str]
    voucher_message: Optional[str]
    voucher_code: Optional[str]
    voucher_expires_timestamp: Optional[int]
    voucher_issue_term_conversion_id: Optional[str]
    voucher_redeem_term_conversion_id: Optional[str]
    term_id: Optional[str]
    address_id: Optional[str]


class VoucherRedeemedEvent(Event):
    aid: Optional[str]
    voucher_id: Optional[str]
    voucher_state: Optional[int]
    voucher_send_date_timestamp: Optional[int]
    voucher_recipient_name: Optional[str]
    voucher_recipient_email: Optional[str]
    voucher_message: Optional[str]
    voucher_code: Optional[str]
    voucher_expires_timestamp: Optional[int]
    voucher_issue_term_conversion_id: Optional[str]
    voucher_redeem_term_conversion_id: Optional[str]
    term_id: Optional[str]
    address_id: Optional[str]


class VoucherRevokedEvent(Event):
    aid: Optional[str]
    voucher_id: Optional[str]
    voucher_state: Optional[int]
    voucher_send_date_timestamp: Optional[int]
    voucher_recipient_name: Optional[str]
    voucher_recipient_email: Optional[str]
    voucher_message: Optional[str]
    voucher_code: Optional[str]
    voucher_expires_timestamp: Optional[int]
    voucher_issue_term_conversion_id: Optional[str]
    voucher_redeem_term_conversion_id: Optional[str]
    term_id: Optional[str]
    address_id: Optional[str]


_E = TypeVar('_E', bound=Event)
_event_types_mapping: Dict[str, Type[_E]] = {
    'unknown': UnknownEvent, 
    'test': TestEvent, 
    'user_payment_method': UserPaymentMethodEvent, 
    'unsupported': UnsupportedEvent, 
    'payment_refund': PaymentRefundEvent, 
    'address_updated': AddressUpdatedEvent, 
    'term_change': TermChangeEvent, 
    'content_algorithm': KeyingEvent, 
    'term_changed': TermChangedEvent, 
    'subscription_auto_renew_changed': SubscriptionAutoRenewChangedByEndUserEvent, 
    'user_address_updated': UserAddressUpdatedEvent, 
    'voucher_redeemed': VoucherRedeemedEvent, 
    'voucher_delivered': VoucherDeliveredEvent, 
    'voucher_revoked': VoucherRevokedEvent, 
    'voucher_purchased': VoucherPurchasedEvent, 
    'user_updated': UserUpdatedEvent, 
    'user_email_confirmed': UserEmailConfirmedEvent, 
    'user_created': UserCreatedEvent, 
    'user_disabled': UserDisabledEvent, 
    'contract_updated': ContractUpdatedEvent, 
    'contract_created': ContractCreatedEvent, 
    'contract_user_created': ContractUserCreatedEvent, 
    'licensee_invite_to_contract': ContractUserInvitedEvent, 
    'contract_deleted': ContractDeletedEvent, 
    'subscription_renewal': SubscriptionRenewalEvent, 
    'access_granted': AccessGrantedEvent, 
    'access_revoked': AccessRevokedEvent, 
    'access_modified': AccessModifiedEvent, 
    'licensee_created': LicenseeCreatedEvent, 
    'licensee_updated': LicenseeUpdatedEvent, 
    'term_change_finished': TermChangeFinishedEvent, 
    'contract_user_access_expired': ContractUserAccessExpiredEvent, 
    'contract_user_access_revoked': ContractUserAccessRevokedEvent, 
    'contract_redeemed': ContractRedeemedEvent, 
    'contract_renewed': ContractRenewedEvent, 
    'shared_subscription_child': SharedSubscriptionChildAccessGrantedEvent
}
