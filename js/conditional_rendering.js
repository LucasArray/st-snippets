function Mailbox({ unreadMessages }) {
    return (
      <div>
        {unreadMessages.length > 0 &&
          <h2>
            You have {unreadMessages.length} unread.
          </h2>
        }
      </div>
    );
  }