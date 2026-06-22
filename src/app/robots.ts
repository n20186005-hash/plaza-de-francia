import { MetadataRoute } from 'next';

export default function robots(): MetadataRoute.Robots {
  const domain = process.env.CURRENT_SITE_DOMAIN || 'www.plazadefranciapanama.com';
  const baseUrl = `https://${domain}`;

  return {
    rules: {
      userAgent: '*',
      allow: '/',
    },
    sitemap: `${baseUrl}/sitemap.xml`,
  };
}
