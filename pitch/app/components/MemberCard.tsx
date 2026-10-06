import type { Member } from "../content";

export function MemberCard({ member }: { member: Member }) {
  return (
    <li className="member-row">
      <h2 className="member-name">{member.name}</h2>
      {member.personal ? <p className="member-personal">{member.personal}</p> : null}
    </li>
  );
}
