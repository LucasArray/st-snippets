import { useState, useEffect } from 'react';

function DocTitleUpdater({ title }) {
  useEffect(() => {
    document.title = title;
  }, [title]);

  return <h2>Title updated!</h2>;
}