A system that manages requests for access-cards.

## Design Decision: Authorized Staff Approval

**Status:** Proposed — pending clarification of the original requirement.

### 1. Identified Ambiguity

The project mission states:

> "A request must be created, approved by an authorized staff identifier, issued and eventually returned."

However, the requirements do not explicitly define what makes a staff identifier authorized or how the application should verify that authorization.

The specification requires a nonempty `approved_by` value before a request can move from `approved` to `issued`. However, a nonempty identifier alone does not establish that it belongs to an authorized staff member.

**Decision:** We will flag this as an ambiguity in the original specification and adopt a staff registry as our proposed interpretation.

### 2. Staff Registry and Authorization

- The application will maintain a staff registry.
- Staff members must be registered before they can approve access-card requests.
- Every staff member in the registry is considered active and authorized to approve requests.
- No distinction between staff roles or permission levels will be implemented.
- Staff members can be registered and removed.
- Attempting to remove a nonexistent staff member must fail.
- Staff identifiers must be unique and must never be reused, even after a staff member is removed.

### 3. Staff Identification

For simplicity, staff members will identify themselves using their registered staff IDs.

The application will check whether the supplied identifier exists in the staff registry before allowing an approval.

**Scope limitation:** This approach verifies staff registration, but it does not securely establish the identity of the person supplying the identifier. Full authentication using additional credentials is outside the current project scope.

### 4. Approval Rules

- Only registered staff members may approve requests.
- An empty staff identifier must be rejected.
- An approval attempt by an unregistered staff member must be rejected.
- A request may only be approved when its current status permits the operation.
- An already approved request cannot be approved again.
- Invalid operations must leave the request record unchanged.

Since all registered staff members are authorized, no role-based permission checks are necessary.

### 5. Historical Approval Records

When a staff member approves a request, the request's `approved_by` field will retain that staff member's ID.

Removing the staff member from the registry must not erase or modify existing approval records.

This preserves historical context, allowing the application to retain the identity recorded at the time of approval even after the staff member has left.

A removed staff member will no longer be authorized to approve new requests.

### 6. Decisions Still to Be Confirmed

The following decisions are outside the immediate scope of this discussion:

- The exact data structure and persistence design for the staff registry.
- The detailed implementation of staff registration and removal.
- How permanently used staff IDs will be tracked.
- How the application will handle inconsistencies in persisted staff data.

These matters will be addressed during the appropriate design phase.

### 7. Rationale

This interpretation keeps the application simple while introducing a clear rule for staff authorization.

A staff registry provides a single reference for determining whether an identifier is currently authorized, while retaining historical approval identifiers preserves the integrity of existing request records.

The design adds staff management to the original project scope without introducing staff roles or a full authentication system.